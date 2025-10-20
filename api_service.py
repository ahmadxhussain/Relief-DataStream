"""
API Service Layer for NGO Data Helpers Streamlit App
Handles communication with backend API for real data sources
"""

import requests
import json
import time
from typing import Dict, List, Optional, Any
from datetime import datetime
import os
from config import get_config

class APIService:
    """Service class for communicating with the backend API"""
    
    def __init__(self):
        self.config = get_config()
        self.base_url = self.config['BACKEND_API_URL']
        self.timeout = self.config['API_TIMEOUT']
        self.poll_interval = self.config['POLL_INTERVAL']
        self.use_mock = self.config['USE_MOCK_DATA']
        
    def fetch_countries(self) -> List[Dict[str, str]]:
        """
        Fetch list of supported countries from backend
        
        Returns:
            List of country dictionaries with 'code' and 'name' keys
        """
        if self.use_mock:
            return self._get_mock_countries()
        
        try:
            response = requests.get(
                f"{self.base_url}/api/countries",
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching countries: {e}")
            # Fallback to mock data on error
            return self._get_mock_countries()
    
    def generate_report(self, country: Dict[str, str], date_range: Dict[str, str]) -> Dict[str, Any]:
        """
        Start report generation process
        
        Args:
            country: Country dict with 'code' and 'name'
            date_range: Date range dict with 'start_date' and 'end_date'
            
        Returns:
            Dict containing report_id and initial status
        """
        if self.use_mock:
            return self._generate_mock_report(country, date_range)
        
        try:
            payload = {
                "country": country,
                "date_range": date_range,
                "language": "en"  # Will be updated to use current language
            }
            
            response = requests.post(
                f"{self.base_url}/api/reports",
                json=payload,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error starting report generation: {e}")
            # Fallback to mock data on error
            return self._generate_mock_report(country, date_range)
    
    def check_report_status(self, report_id: str) -> Dict[str, Any]:
        """
        Check the status of a report generation
        
        Args:
            report_id: Unique identifier for the report
            
        Returns:
            Dict containing status, progress, and current step
        """
        if self.use_mock:
            return self._get_mock_status(report_id)
        
        try:
            response = requests.get(
                f"{self.base_url}/api/reports/{report_id}/status",
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error checking report status: {e}")
            return {"status": "error", "message": str(e)}
    
    def get_report_data(self, report_id: str) -> Optional[Dict[str, Any]]:
        """
        Get the complete report data
        
        Args:
            report_id: Unique identifier for the report
            
        Returns:
            Dict containing complete report data or None if not ready
        """
        if self.use_mock:
            return self._get_mock_report_data(report_id)
        
        try:
            response = requests.get(
                f"{self.base_url}/api/reports/{report_id}",
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching report data: {e}")
            return None
    
    def download_report(self, report_id: str, format: str) -> bool:
        """
        Download report in specified format
        
        Args:
            report_id: Unique identifier for the report
            format: 'pdf' or 'docx'
            
        Returns:
            True if download successful, False otherwise
        """
        if self.use_mock:
            return self._mock_download(format)
        
        try:
            response = requests.get(
                f"{self.base_url}/api/reports/{report_id}/download",
                params={"format": format},
                timeout=self.timeout
            )
            response.raise_for_status()
            
            # Save file locally
            filename = f"report_{report_id}.{format}"
            with open(filename, 'wb') as f:
                f.write(response.content)
            
            print(f"Report downloaded as {filename}")
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error downloading report: {e}")
            return False
    
    def poll_report_completion(self, report_id: str, max_wait_time: int = 300) -> Dict[str, Any]:
        """
        Poll for report completion with progress updates
        
        Args:
            report_id: Unique identifier for the report
            max_wait_time: Maximum time to wait in seconds
            
        Returns:
            Final report data when complete
        """
        start_time = time.time()
        
        while time.time() - start_time < max_wait_time:
            status = self.check_report_status(report_id)
            
            if status.get("status") == "completed":
                return self.get_report_data(report_id)
            elif status.get("status") == "error":
                return {"error": status.get("message", "Unknown error")}
            
            # Yield control for UI updates
            time.sleep(self.poll_interval)
        
        return {"error": "Report generation timed out"}
    
    # Mock data methods (fallback when backend unavailable)
    
    def _get_mock_countries(self) -> List[Dict[str, str]]:
        """Get mock country data"""
        return [
            {'code': 'AF', 'name': 'Afghanistan'},
            {'code': 'AL', 'name': 'Albania'},
            {'code': 'DZ', 'name': 'Algeria'},
            {'code': 'AO', 'name': 'Angola'},
            {'code': 'AR', 'name': 'Argentina'},
            {'code': 'AM', 'name': 'Armenia'},
            {'code': 'AU', 'name': 'Australia'},
            {'code': 'AT', 'name': 'Austria'},
            {'code': 'AZ', 'name': 'Azerbaijan'},
            {'code': 'BD', 'name': 'Bangladesh'},
            {'code': 'BR', 'name': 'Brazil'},
            {'code': 'CA', 'name': 'Canada'},
            {'code': 'CN', 'name': 'China'},
            {'code': 'FR', 'name': 'France'},
            {'code': 'DE', 'name': 'Germany'},
            {'code': 'IN', 'name': 'India'},
            {'code': 'IT', 'name': 'Italy'},
            {'code': 'JP', 'name': 'Japan'},
            {'code': 'MX', 'name': 'Mexico'},
            {'code': 'NG', 'name': 'Nigeria'},
            {'code': 'PK', 'name': 'Pakistan'},
            {'code': 'RU', 'name': 'Russia'},
            {'code': 'SA', 'name': 'Saudi Arabia'},
            {'code': 'ZA', 'name': 'South Africa'},
            {'code': 'KR', 'name': 'South Korea'},
            {'code': 'ES', 'name': 'Spain'},
            {'code': 'TR', 'name': 'Turkey'},
            {'code': 'GB', 'name': 'United Kingdom'},
            {'code': 'US', 'name': 'United States'},
        ]
    
    def _generate_mock_report(self, country: Dict[str, str], date_range: Dict[str, str]) -> Dict[str, Any]:
        """Generate mock report with simulated processing"""
        report_id = f"mock_{int(time.time())}"
        return {
            "report_id": report_id,
            "status": "processing",
            "message": "Report generation started",
            "country": country,
            "date_range": date_range,
            "created_at": datetime.now().isoformat()
        }
    
    def _get_mock_status(self, report_id: str) -> Dict[str, Any]:
        """Get mock status for report"""
        return {
            "status": "completed",
            "progress": 100,
            "current_step": "ready",
            "message": "Report generation completed"
        }
    
    def _get_mock_report_data(self, report_id: str) -> Dict[str, Any]:
        """Get mock report data"""
        import random
        
        chart_data = [
            {'name': 'Jan', 'value': random.randint(20, 120), 'date': '2024-01-01'},
            {'name': 'Feb', 'value': random.randint(20, 120), 'date': '2024-02-01'},
            {'name': 'Mar', 'value': random.randint(20, 120), 'date': '2024-03-01'},
            {'name': 'Apr', 'value': random.randint(20, 120), 'date': '2024-04-01'},
            {'name': 'May', 'value': random.randint(20, 120), 'date': '2024-05-01'},
            {'name': 'Jun', 'value': random.randint(20, 120), 'date': '2024-06-01'},
        ]
        
        return {
            "summary": "This is a mock report generated for testing purposes. In production, this would contain real data from ACLED, GDELT, ReliefWeb, and WorldBank APIs processed through RAG and LLM generation.",
            "key_events": [
                "Mock event 1: Major policy changes announced",
                "Mock event 2: International aid programs launched",
                "Mock event 3: Economic indicators show mixed results",
                "Mock event 4: New partnerships established",
                "Mock event 5: Climate-related challenges continue"
            ],
            "trends": [
                "Mock trend 1: Gradual improvement in education access",
                "Mock trend 2: Healthcare infrastructure showing positive development",
                "Mock trend 3: Economic stability remains a concern",
                "Mock trend 4: Technology adoption increasing",
                "Mock trend 5: Environmental sustainability initiatives gaining momentum"
            ],
            "risks": [
                "Mock risk 1: Political instability may affect programs",
                "Mock risk 2: Economic volatility could impact funding",
                "Mock risk 3: Climate change continues to pose challenges",
                "Mock risk 4: Resource constraints may limit expansion",
                "Mock risk 5: Security concerns affecting aid delivery"
            ],
            "chart_data": chart_data,
            "sources": [
                "ACLED (Mock Data)",
                "GDELT (Mock Data)", 
                "ReliefWeb (Mock Data)",
                "WorldBank (Mock Data)"
            ],
            "generated_at": datetime.now().isoformat(),
            "report_id": report_id
        }
    
    def _mock_download(self, format: str) -> bool:
        """Simulate download process"""
        print(f"Mock download initiated for {format.upper()} format")
        return True

# Global API service instance
api_service = APIService()
