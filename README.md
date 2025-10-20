# NGO Data Helpers - Streamlit Frontend

A Streamlit-based front-end application for NGO data helpers to generate comprehensive humanitarian and development reports.

## Features

- **Country Selection**: Choose from 195+ countries
- **Date Range Selection**: Pick custom start and end dates
- **Progress Tracking**: Real-time progress indicators during report generation
- **Report Preview**: Comprehensive reports with summaries, key events, trends, and risks
- **Data Visualization**: Interactive charts and graphs using Plotly
- **Download Options**: Export reports in PDF or DOCX format (mock)
- **Error Handling**: Clear error messages and user guidance
- **Multi-language Support**: Language selection interface
- **Report History**: View and manage previously generated reports
- **Responsive Design**: Works on desktop and mobile devices

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ahmadxhussain/Relief-DataStream.git
   cd Relief-DataStream
   ```

2. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

3. Run the Streamlit application:
   ```bash
   python -m streamlit run app.py
   ```

4. Open your browser and navigate to `http://localhost:8501`

### Windows PowerShell Note
If you get `CommandNotFoundException` errors, use the `python -m` approach shown above, which bypasses PATH issues on Windows.

## Usage

1. **Select Country and Dates**: Choose a country from the dropdown and select your desired date range
2. **Build Report**: Click the "Build Report" button to generate your report
3. **Monitor Progress**: Watch the progress indicators as the system processes your request
4. **Preview Report**: Review the generated report with summaries, events, trends, and charts
5. **Download**: Choose your preferred format (PDF or DOCX) and download the report
6. **View History**: Access previously generated reports from the History page
7. **Settings**: Change language preferences and other settings

## Technology Stack

- **Streamlit** - Web application framework
- **Python 3.8+** - Programming language
- **Pandas** - Data manipulation
- **Plotly** - Interactive data visualization
- **NumPy** - Numerical computing
- **Requests** - HTTP API communication
- **Python-dotenv** - Environment configuration
- **ReportLab** - PDF generation
- **Python-docx** - DOCX generation

## Project Structure

```
├── app.py                 # Main Streamlit application
├── api_service.py         # Backend API communication
├── config.py             # Configuration management
├── translations.py        # Multi-language support
├── requirements.txt      # Python dependencies
├── env.example          # Environment template
├── API_CONTRACT.md      # Backend API documentation
└── README.md            # This file
```

## Features Implemented

### Core Features (B-001 through B-010)
- ✅ **B-001**: Country and Date Inputs + Build Report Button
- ✅ **B-002**: Progress Bar/Steps with real-time updates
- ✅ **B-003**: Report Preview with text sections and charts
- ✅ **B-004**: Download buttons for PDF/DOCX
- ✅ **B-005**: Error banner with clear messaging
- ✅ **B-006**: Clear/Reset functionality
- ✅ **B-007**: Help/About page with comprehensive guide
- ✅ **B-010**: Navigation between all screens

### Stretch Goals
- ✅ **B-008**: Settings page with language picker and dark mode
- ✅ **B-009**: History screen with saved reports management

### Backend Integration (B-011)
- ✅ **API Service Layer**: Complete backend communication system
- ✅ **Environment Configuration**: Flexible configuration management
- ✅ **Mock Data Fallback**: Graceful fallback when backend unavailable
- ✅ **Error Handling**: Comprehensive error handling and retry logic
- ✅ **Progress Tracking**: Real-time progress for long-running operations
- ✅ **API Contract**: Complete documentation for backend team

## Backend Integration

The frontend is **ready for backend integration**! Currently runs in **mock mode** by default.

### Environment Configuration

Create a `.env` file (copy from `env.example`):
```bash
# Backend API Configuration
BACKEND_API_URL=http://localhost:8000
API_TIMEOUT=120
POLL_INTERVAL=2
USE_MOCK_DATA=true

# API Keys (for backend team)
ACLED_API_KEY=your_acled_api_key_here
GDELT_API_KEY=your_gdelt_api_key_here
RELIEFWEB_API_KEY=your_reliefweb_api_key_here
WORLDBANK_API_KEY=your_worldbank_api_key_here
```

### Switching to Real Backend

1. Set `USE_MOCK_DATA=false` in `.env`
2. Ensure backend is running on `BACKEND_API_URL`
3. Restart the Streamlit app

### API Contract

See `API_CONTRACT.md` for detailed backend API requirements.

## Mock Data (Current Mode)

The application currently uses mock data that simulates:
- Country selection from 29 countries (expandable)
- Report generation with realistic delays
- Sample humanitarian and development data
- Interactive charts with random but realistic data points
- Report sections: Summary, Key Events, Trends, Risks

## Development

### Frontend Complete ✅
All builds B-001 through B-010 are complete including stretch goals:
- Multi-language support (4 languages)
- Dark/Light mode theming
- Real-time language and theme switching
- Session persistence
- Responsive design
- API service layer ready

### Backend Integration Ready ✅
The frontend will connect with:
- **Data Sources**: ACLED, GDELT, ReliefWeb, WorldBank APIs
- **Processing**: LangChain for chunking, ChromaDB for vector storage, RAG retrieval
- **LLM**: Ollama for report generation with inline citations
- **Output**: Structured reports with charts, exportable as DOCX/PDF

### Next Steps
1. **Backend Team**: Implement API endpoints per `API_CONTRACT.md`
2. **Integration**: Set `USE_MOCK_DATA=false` when backend is ready
3. **Testing**: Test with real data sources
4. **Deployment**: Deploy both frontend and backend

## License

This project is part of the UTD Fall Project 2025 Capstone.