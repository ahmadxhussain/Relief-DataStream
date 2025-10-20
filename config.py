"""
Configuration module for NGO Data Helpers Streamlit App
Handles environment variables and app settings
"""

import os
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_config() -> Dict[str, Any]:
    """
    Get application configuration from environment variables
    
    Returns:
        Dict containing all configuration settings
    """
    return {
        # Backend API Configuration
        'BACKEND_API_URL': os.getenv('BACKEND_API_URL', 'http://localhost:8000'),
        'API_TIMEOUT': int(os.getenv('API_TIMEOUT', '120')),  # seconds
        'POLL_INTERVAL': int(os.getenv('POLL_INTERVAL', '2')),  # seconds
        'USE_MOCK_DATA': os.getenv('USE_MOCK_DATA', 'true').lower() == 'true',
        
        # API Keys (for backend team to implement)
        'ACLED_API_KEY': os.getenv('ACLED_API_KEY', ''),
        'GDELT_API_KEY': os.getenv('GDELT_API_KEY', ''),
        'RELIEFWEB_API_KEY': os.getenv('RELIEFWEB_API_KEY', ''),
        'WORLDBANK_API_KEY': os.getenv('WORLDBANK_API_KEY', ''),
        
        # LLM Configuration
        'OLLAMA_BASE_URL': os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434'),
        'OLLAMA_MODEL': os.getenv('OLLAMA_MODEL', 'llama2'),
        
        # Database Configuration
        'CHROMA_PERSIST_DIRECTORY': os.getenv('CHROMA_PERSIST_DIRECTORY', './chroma_db'),
        
        # App Configuration
        'APP_TITLE': os.getenv('APP_TITLE', 'NGO Data Helpers'),
        'APP_VERSION': os.getenv('APP_VERSION', '1.0.0'),
        'DEBUG': os.getenv('DEBUG', 'false').lower() == 'true',
        
        # File Storage
        'REPORTS_DIRECTORY': os.getenv('REPORTS_DIRECTORY', './reports'),
        'MAX_REPORT_SIZE_MB': int(os.getenv('MAX_REPORT_SIZE_MB', '50')),
        
        # Rate Limiting
        'RATE_LIMIT_REQUESTS_PER_MINUTE': int(os.getenv('RATE_LIMIT_REQUESTS_PER_MINUTE', '60')),
        'RATE_LIMIT_REPORTS_PER_HOUR': int(os.getenv('RATE_LIMIT_REPORTS_PER_HOUR', '10')),
    }

def get_api_config() -> Dict[str, str]:
    """
    Get API-specific configuration
    
    Returns:
        Dict containing API configuration
    """
    config = get_config()
    return {
        'base_url': config['BACKEND_API_URL'],
        'timeout': str(config['API_TIMEOUT']),
        'poll_interval': str(config['POLL_INTERVAL']),
        'use_mock': str(config['USE_MOCK_DATA']).lower(),
    }

def get_llm_config() -> Dict[str, str]:
    """
    Get LLM-specific configuration
    
    Returns:
        Dict containing LLM configuration
    """
    config = get_config()
    return {
        'ollama_base_url': config['OLLAMA_BASE_URL'],
        'ollama_model': config['OLLAMA_MODEL'],
        'chroma_persist_directory': config['CHROMA_PERSIST_DIRECTORY'],
    }

def get_data_source_config() -> Dict[str, str]:
    """
    Get data source API keys
    
    Returns:
        Dict containing API keys for data sources
    """
    config = get_config()
    return {
        'acled_api_key': config['ACLED_API_KEY'],
        'gdelt_api_key': config['GDELT_API_KEY'],
        'reliefweb_api_key': config['RELIEFWEB_API_KEY'],
        'worldbank_api_key': config['WORLDBANK_API_KEY'],
    }

def is_development() -> bool:
    """
    Check if running in development mode
    
    Returns:
        True if development mode, False otherwise
    """
    return get_config()['DEBUG']

def is_mock_mode() -> bool:
    """
    Check if running in mock data mode
    
    Returns:
        True if using mock data, False if using real backend
    """
    return get_config()['USE_MOCK_DATA']

# Export commonly used configs
config = get_config()
api_config = get_api_config()
llm_config = get_llm_config()
data_source_config = get_data_source_config()
