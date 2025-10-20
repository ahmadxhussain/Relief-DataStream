# Streamlit Frontend Backend Integration Preparation (B-011)

## Current State
All frontend features (B-001 through B-010) are complete including stretch goals. The Streamlit app uses mock data from `generate_mock_report_data()` function.

## Backend Architecture Context
The backend will use **Streamlit + Python** with:
- **Data Sources**: ACLED, GDELT, ReliefWeb, WorldBank APIs
- **Processing**: LangChain for chunking, ChromaDB for vector storage, RAG retrieval
- **LLM**: Ollama for report generation with inline citations
- **Output**: Structured reports (Summary, Events, Trends, Risks) with charts, exportable as DOCX/PDF

This Streamlit frontend will communicate with the backend via HTTP API calls.

## Goals
- Create a clean API service layer in Python for backend communication
- Add environment configuration for backend URL and settings
- Replace mock data usage with API service calls
- Support long-running operations (RAG + LLM can take 30-60s+)
- Add proper error handling for network and backend processing errors
- Document expected API contract for backend team to implement

## Implementation Steps

### 1. Create API Service Layer
**File: `api_service.py`**
- Create Python functions for all API methods:
  - `fetch_countries()` - Get list of supported countries
  - `generate_report(country, date_range)` - POST to backend to trigger report generation
  - `check_report_status(report_id)` - Poll for progress updates during RAG/LLM processing
  - `download_report(report_id, format)` - Download PDF or DOCX
- Implement dual mode: mock data (current) vs real backend calls
- Add proper error handling, retry logic, and timeout management
- Support polling for real-time progress updates

### 2. Environment Configuration
**File: `.env.example` and `config.py`**
- Add `BACKEND_API_URL` - Backend API URL (e.g., `http://localhost:8000`)
- Add `API_TIMEOUT` - Request timeout (120000ms for RAG/LLM operations)
- Add `USE_MOCK_DATA` - Toggle between mock and real backend (true for dev, false for prod)
- Add `POLL_INTERVAL` - How often to check report generation status (2000ms)
- Document all variables in README with examples

### 3. Update app.py to Use API Service
**File: `app.py`**
- Replace `generate_mock_report_data()` with `api_service.generate_report()`
- Add polling mechanism to track backend progress (Collecting → Processing → Summarizing → Ready)
- Replace static `COUNTRIES` with `api_service.fetch_countries()` on mount
- Update download handlers to call `api_service.download_report(report_id, format)`
- Handle long-running operations (RAG retrieval + Ollama generation can take 30-60s+)
- Add better error messages for network failures vs backend processing errors

### 4. Create API Documentation
**File: `API_CONTRACT.md`**
- Document expected backend endpoints:
  - `GET /api/countries` - Returns list of supported countries
  - `POST /api/reports` - Starts report generation, returns reportId
  - `GET /api/reports/{reportId}/status` - Returns progress & current step
  - `GET /api/reports/{reportId}` - Returns complete report data (JSON)
  - `GET /api/reports/{reportId}/download?format=pdf|docx` - Download file
- Specify request/response formats with Python data structures
- Document expected processing steps for progress tracking
- Include error codes (400, 404, 500, 503) and handling strategies
- Add example payloads and responses

### 5. Enhance Progress Tracking
**File: Update app.py for real backend operations**
- Modify progress steps to reflect actual backend pipeline stages:
  - "Collecting Data" - Fetching from ACLED, GDELT, ReliefWeb, WorldBank
  - "Processing" - Normalizing, chunking, creating embeddings
  - "Generating Report" - RAG retrieval + Ollama summarization
  - "Ready" - Report complete with citations
- Add estimated time remaining based on backend feedback
- Handle timeouts gracefully (RAG/LLM can be slow)
- Add retry button if generation fails mid-process
- Show data source status (which APIs succeeded/failed)

## Files to Create
- `api_service.py` - Main API service with mock/real mode
- `config.py` - Configuration and environment variables
- `.env.example` - Environment variable template
- `API_CONTRACT.md` - Backend API documentation for backend team

## Files to Modify
- `app.py` - Use API service, add polling for progress
- `requirements.txt` - Add requests, python-dotenv dependencies
- `README.md` - Add backend integration instructions

## Benefits
- Backend team has clear API contract to implement
- Frontend works with mock data until backend is ready
- Simple environment variable change to connect to real backend
- Handles long-running RAG/LLM operations gracefully
- Clean separation allows parallel frontend/backend development
- Easy to test both modes independently

## Current Streamlit Features Complete
✅ All builds B-001 through B-010 implemented
✅ Multi-language support (4 languages)
✅ Dark mode (Light/Dark themes)
✅ Real-time language and theme switching
✅ Session persistence
✅ Responsive design
✅ Mock data generation
✅ Progress tracking
✅ Error handling
✅ Report preview with charts
✅ Download functionality (mock)
✅ History management
✅ Settings page

## Next Steps
1. Create Python API service layer
2. Add environment configuration
3. Update Streamlit app to use API service
4. Create API documentation for backend team
5. Test integration with mock backend
6. Ready for backend team integration
