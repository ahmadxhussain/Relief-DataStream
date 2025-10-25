import torch
import os
from huggingface_hub import login
from transformers import pipeline, AutoTokenizer
import pycountry
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Set your tokens as environment variables
HF_TOKEN = os.getenv('HF_TOKEN')
G_NEWS_TOKEN = os.getenv('G_NEWS_TOKEN')
ACLED_USERNAME = os.getenv('ACLED_USERNAME')
ACLED_PASSWORD = os.getenv('ACLED_PASSWORD')

class LlamaService:
    def __init__(self):
        self.base_prompt = """
        You are an expert humanitarian data analyst working for an NGO.

        TASK:
        Analyze socioeconomic and humanitarian data provided from multiple datasets and produce concise, structured insights.

        STRICT RULES:
        1. Ground every statement strictly in the provided data. Never guess or infer missing information.
        2. Ignore and exclude any NaN, null, or missing values completely.
        3. Discuss only data related to the specified country.
        4. Do NOT give any recommendations, opinions, or projections.
        5. Write your entire output in ENGLISH only.
        6. Include citations inline using this exact format:
           - (World Bank)
           - (ReliefWeb)
           - (Google News)
           - (ACLED)
           Do not invent or include any other sources.
        7. Keep the tone formal, analytical, and data-driven.
        8. Do not repeat any data or information.

        OUTPUT FORMAT:
        **Executive Summary**
        - Provide a concise overview (1–2 paragraphs) summarizing key humanitarian and socioeconomic conditions.

        **Key Events**
        - Summarize 4–6 major factual developments (conflict, migration, disasters, economic shifts, disease, immigration, or war) with inline citations.

        **Trends**
        - Discuss observable trends in population, economy, displacement, and aid response, grounded in the data.

        **Risks**
        - Identify emerging or ongoing humanitarian risks (conflict escalation, funding gaps, or instability) strictly from the data.
        """
        
        # Initialize model (cache it to avoid reloading)
        self.model = None
        self.tokenizer = None
        self.llama_pipeline = None
        
    def initialize_model(self):
        """Initialize the Llama model (call this once)"""
        if self.llama_pipeline is not None:
            return
            
        login(HF_TOKEN)
        model_name = "meta-llama/Llama-3.2-3B-Instruct"
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.llama_pipeline = pipeline(
            "text-generation",
            model=model_name,
            dtype=torch.bfloat16,
            device_map="auto",
            tokenizer=self.tokenizer,
            do_sample=False,
            repetition_penalty=1.15,
            return_full_text=False,
            pad_token_id=self.tokenizer.eos_token_id,
            max_new_tokens=1024
        )

    # Your existing API functions (copy from Colab)
    def fetch_worldbank(self, country, indicator, start, end):
        url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}"
        params = {
            "date": f"{start}:{end}",
            "format": "json"
        }
        response = requests.get(url, params)
        if response.status_code != 200:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
        response = response.json()
        df = pd.json_normalize(response[1])
        return df[["indicator.id", "indicator.value", "date", "value"]]

    def fetch_indicators(self, country, start, end):
        indicators = {
            "SP.POP.TOTL": "Total population",
            "SP.POP.GROW": "Population growth (annual %)",
            "NY.GDP.MKTP.CD": "GDP (current US$)",
            "NY.GDP.MKTP.KD.ZG": "GDP growth (annual %)",
            "NY.GDP.PCAP.CD": "GDP per capita (current US$)",
            "SL.UEM.TOTL.ZS": "Unemployment, total (% of labor force)",
            "FP.CPI.TOTL.ZG": "Inflation, consumer prices (annual %)",
        }
        dfs = []
        for i in indicators.keys():
            df = self.fetch_worldbank(country, i, start, end)
            if df is not None:
                dfs.append(df)
        if not dfs:
            return pd.DataFrame()
        df = pd.concat(dfs)
        df = df.pivot(index="date", columns="indicator.id", values="value")
        df = df.rename(columns=indicators)
        return df

    def create_prompt_worldbank(self, country, start, end):
        df = self.fetch_indicators(country, start, end)
        if df.empty:
            return f"No World Bank data available for {country} in the specified period."
        
        prompt = f""" This is data for {country} in {end} from the World Bank API:"""
        for col in df.columns:
            prompt += f"\n  - {col}: {df[col].iloc[0] if not df.empty else 'N/A'}"
        prompt += "\n  - If any data is NaN, do not include it in the summary."
        return prompt

    def clean_html(self, input_text):
        if not input_text:
            return ""
        soup = BeautifulSoup(input_text, "html.parser")
        for br in soup.find_all("br"):
            br.replace_with("\n")
        for p in soup.find_all("p"):
            p.insert_after("\n")
        text = soup.get_text(" ", strip=True)
        return text

    def fetch_reliefweb(self, country, start, end):
        url = "https://api.reliefweb.int/v1/reports?appname=relief-datastream"
        limit = 100
        payload = {
            "filter": {
                "operator": "AND",
                "conditions": [
                    {"field": "country.name", "value": country},
                    {"field": "date.created", "value": {"from": f"{start}T00:00:00+00:00", "to": f"{end}T23:59:59+00:00"}},
                    {"field": "language.name", "value": "English"}
                ]
            },
            "profile": "full",
            "limit": limit,
            "offset": 0
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json().get("data", [])
        reports = []
        for item in data:
            f = item["fields"]
            reports.append({
                "title": f.get("title"),
                "date": f.get("date", {}).get("original", "").replace("T00:00:00+00:00", ""),
                "source": ", ".join([s["name"] for s in f.get("source", [])]),
                "body": self.clean_html(f.get("body")),
            })
        content = ""
        for report in reports:
            content += f"""
                Title: {report['title'].strip()}
                Date: {report['date'].strip()}
                Source: {report['source'].strip()}
                Article Content: {report['body'].strip()}
                \n
            """
        return content

    def create_prompt_reliefweb(self, country, start, end):
        content = self.fetch_reliefweb(country, start, end)
        prompt = f""" These are multiple articles for {country} These articles were published between {start} and {end} from ReliefWeb API:
        {content}
        """
        return prompt

    def fetch_gnews(self, query, start, end, api_key):
        url = "https://gnews.io/api/v4/search"
        all_articles = []
        page = 1
        while True:
            params = {
                "q": query,
                "lang": "en",
                "from": start,
                "to": end,
                "max": 100,
                "page": page,
                "token": api_key
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            articles = data.get("articles", [])
            if not articles:
                break
            all_articles.extend(articles)
            if len(articles) < 100:
                break
            page += 1
        if not all_articles:
            return pd.DataFrame(columns=["source", "title", "date", "url", "description"])
        df = pd.json_normalize(all_articles)
        df = df.rename(columns={
            "source.name": "source",
            "title": "title",
            "publishedAt": "date",
            "url": "url",
            "description": "description"
        })
        df["date"] = pd.to_datetime(df["date"]).dt.date
        return df[["source", "title", "date", "url", "description"]]

    def create_prompt_gnews(self, country, start, end):
        df = self.fetch_gnews(country, start, end, G_NEWS_TOKEN)
        if df.empty:
            return f"No Google News articles found for {country} between {start} and {end}."
        content = ""
        for row in df.itertuples(index=False):
            content += f"""
                Title: {row.title.strip()}
                Date: {row.date}
                Source: {row.source.strip()}
                Article Content: {row.description.strip()}
                \n
            """
        prompt = f""" These are multiple articles for {country} These articles were published between {start} and {end} from Google News API:
        {content}
        """
        return prompt

    def request_oauth(self, username, password):
        payload = {
            "username": username,
            "password": password,
            "grant_type": "password",
            "client_id": "acled"
        }
        response = requests.post("https://acleddata.com/oauth/token", data=payload)
        response = response.json()
        return response["access_token"]

    def fetch_fatalities(self, country, start, end):
        token = self.request_oauth(ACLED_USERNAME, ACLED_PASSWORD)
        headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
        params = {
            "_format": "json",
            "country": country,
            "event_date": f"{start}|{end}",
            "event_date_where": "BETWEEN"
        }
        response = requests.get("https://acleddata.com/api/acled/read", headers=headers, params=params)
        response = response.json()
        df = pd.json_normalize(response['data'])
        return df

    def create_prompt_acled(self, country, start, end):
        df = self.fetch_fatalities(country, start, end)
        if df.empty:
            return f"No recorded fatalities from political violence by ACLED for {country} between {start} and {end}."
        content = f"These are events with recorded fatalities by ACLED in {country} between {start} and {end}:\n"
        for row in df.itertuples(index=False):
            content += f"""
    Date: {row.event_date}
    Description: {row.notes}
    Fatalities: {row.fatalities}
    """
        return content

    def generate_report(self, country_name, date_range):
        """Main function to generate report using Llama"""
        try:
            # Initialize model if not already done
            self.initialize_model()
            
            # Get country code
            country_code = pycountry.countries.lookup(country_name).alpha_3
            start = date_range['start_date']
            end = date_range['end_date']
            
            # Fetch data from all sources
            prompt1 = self.create_prompt_worldbank(country_code, start.split('-')[0], end.split('-')[0])
            prompt2 = self.create_prompt_reliefweb(country_name, start, end)
            prompt3 = self.create_prompt_gnews(country_name, start, end)
            prompt4 = self.create_prompt_acled(country_name, start, end)
            
            text = f"{prompt1} \n {prompt4} \n {prompt2} \n {prompt3}"
            
            # Process with RAG
            splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
            chunks = splitter.create_documents([text])
            
            embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
            chroma = Chroma.from_documents(
                documents=chunks,
                embedding=embedding_model,
            )
            
            STATIC_QUERY = f"""
            Gather comprehensive humanitarian, socioeconomic, and situational information for {country_name}
            from datasets and reports published by the World Bank, ReliefWeb, ACLED, and Google News.
            """
            
            retriever = chroma.as_retriever(
                search_type="mmr",
                search_kwargs={"k": 25, "fetch_k": 60, "lambda_mult": 0.7}
            )
            relevant_docs = retriever.invoke(STATIC_QUERY)
            context = "\n\n".join([doc.page_content for doc in relevant_docs])
            
            # Generate response with Llama
            messages = [
                {"role": "system", "content": self.base_prompt},
                {"role": "user", "content": f"\nRelevant data about {country_name}: {context}"}
            ]
            
            outputs = self.llama_pipeline(messages, max_new_tokens=1500)
            output = outputs[0]["generated_text"]
            
            # Parse the output into structured format
            return self.parse_llama_output(output)
            
        except Exception as e:
            return {"error": f"Failed to generate report: {str(e)}"}

    def parse_llama_output(self, output):
        """Parse Llama output into structured format for your Streamlit app"""
        # Simple parsing - you might want to make this more robust
        sections = {
            'summary': '',
            'key_events': [],
            'trends': [],
            'risks': []
        }
        
        current_section = None
        for line in output.split('\n'):
            line = line.strip()
            if not line:
                continue
                
            if '**Executive Summary**' in line:
                current_section = 'summary'
            elif '**Key Events**' in line:
                current_section = 'key_events'
            elif '**Trends**' in line:
                current_section = 'trends'
            elif '**Risks**' in line:
                current_section = 'risks'
            elif current_section == 'summary' and line and not line.startswith('**'):
                sections['summary'] += line + ' '
            elif current_section in ['key_events', 'trends', 'risks'] and line.startswith('-'):
                item = line[1:].strip()
                if item:
                    sections[current_section].append(item)
        
        # Add mock chart data (you can enhance this with real data)
        sections['chart_data'] = [
            {'name': 'Jan', 'value': 45, 'date': '2024-01-01'},
            {'name': 'Feb', 'value': 78, 'date': '2024-02-01'},
            {'name': 'Mar', 'value': 92, 'date': '2024-03-01'},
            {'name': 'Apr', 'value': 65, 'date': '2024-04-01'},
            {'name': 'May', 'value': 88, 'date': '2024-05-01'},
            {'name': 'Jun', 'value': 76, 'date': '2024-06-01'},
        ]
        
        return sections

# Global instance
llama_service = LlamaService()