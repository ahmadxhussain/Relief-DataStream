# API Contract for NGO Data Helpers Backend

This document defines the API contract that the backend team needs to implement for the NGO Data Helpers Streamlit frontend.

## Base URL
```
http://localhost:8000
```

## Authentication
Currently no authentication required. Future versions may include API key authentication.

## Endpoints

### 1. Get Supported Countries
**GET** `/api/countries`

Returns list of countries supported by the system.

**Response:**
```json
[
  {
    "code": "AF",
    "name": "Afghanistan"
  },
  {
    "code": "AL", 
    "name": "Albania"
  }
]
```

**Status Codes:**
- `200` - Success
- `500` - Server error

---

### 2. Start Report Generation
**POST** `/api/reports`

Starts the report generation process for a specific country and date range.

**Request Body:**
```json
{
  "country": {
    "code": "AF",
    "name": "Afghanistan"
  },
  "date_range": {
    "start_date": "2024-01-01",
    "end_date": "2024-06-30"
  },
  "language": "en"
}
```

**Response:**
```json
{
  "report_id": "report_1234567890",
  "status": "processing",
  "message": "Report generation started",
  "country": {
    "code": "AF",
    "name": "Afghanistan"
  },
  "date_range": {
    "start_date": "2024-01-01",
    "end_date": "2024-06-30"
  },
  "created_at": "2024-01-15T10:30:00Z"
}
```

**Status Codes:**
- `201` - Report generation started
- `400` - Invalid request (missing country, invalid date range)
- `500` - Server error

---

### 3. Check Report Status
**GET** `/api/reports/{report_id}/status`

Check the current status of a report generation.

**Response:**
```json
{
  "status": "processing",
  "progress": 75,
  "current_step": "summarizing",
  "message": "Generating report summary with LLM",
  "estimated_time_remaining": 30,
  "data_sources": {
    "acled": "completed",
    "gdelt": "completed", 
    "reliefweb": "completed",
    "worldbank": "completed"
  }
}
```

**Status Values:**
- `processing` - Report is being generated
- `completed` - Report is ready
- `error` - Report generation failed

**Progress Steps:**
- `collecting` - Fetching data from APIs
- `processing` - Normalizing and chunking data
- `summarizing` - RAG retrieval and LLM generation
- `ready` - Report complete

**Status Codes:**
- `200` - Success
- `404` - Report not found
- `500` - Server error

---

### 4. Get Complete Report Data
**GET** `/api/reports/{report_id}`

Returns the complete report data when generation is finished.

**Response:**
```json
{
  "report_id": "report_1234567890",
  "status": "completed",
  "summary": "This report provides an analysis of humanitarian and development indicators...",
  "key_events": [
    "Major policy changes announced in Afghanistan affecting development priorities",
    "International aid programs launched targeting vulnerable populations"
  ],
  "trends": [
    "Gradual improvement in education access indicators",
    "Healthcare infrastructure showing positive development"
  ],
  "risks": [
    "Political instability may affect ongoing development programs",
    "Economic volatility could impact funding availability"
  ],
  "chart_data": [
    {
      "name": "Jan",
      "value": 85,
      "date": "2024-01-01"
    }
  ],
  "sources": [
    "ACLED - Armed Conflict Location & Event Data Project",
    "GDELT - Global Database of Events, Language, and Tone",
    "ReliefWeb - Humanitarian Information Service",
    "World Bank Open Data"
  ],
  "generated_at": "2024-01-15T10:45:00Z",
  "country": {
    "code": "AF",
    "name": "Afghanistan"
  },
  "date_range": {
    "start_date": "2024-01-01",
    "end_date": "2024-06-30"
  }
}
```

**Status Codes:**
- `200` - Success
- `404` - Report not found
- `202` - Report still processing
- `500` - Server error

---

### 5. Download Report
**GET** `/api/reports/{report_id}/download`

Download the report in PDF or DOCX format.

**Query Parameters:**
- `format` - `pdf` or `docx`

**Response:**
- Content-Type: `application/pdf` or `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
- Content-Disposition: `attachment; filename="report_1234567890.pdf"`

**Status Codes:**
- `200` - Success
- `404` - Report not found
- `400` - Invalid format
- `500` - Server error

---

## Error Response Format

All error responses should follow this format:

```json
{
  "error": {
    "code": "INVALID_DATE_RANGE",
    "message": "End date must be after start date",
    "details": "The provided date range is invalid"
  }
}
```

## Common Error Codes

- `INVALID_COUNTRY` - Country code not supported
- `INVALID_DATE_RANGE` - Invalid date range provided
- `REPORT_NOT_FOUND` - Report ID does not exist
- `GENERATION_FAILED` - Report generation failed
- `API_RATE_LIMIT` - Too many requests
- `DATA_SOURCE_ERROR` - Error fetching from data sources
- `LLM_ERROR` - Error in LLM processing

## Rate Limiting

- **Requests per minute**: 60
- **Reports per hour**: 10
- **Concurrent reports**: 5

Rate limit headers:
```
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 59
X-RateLimit-Reset: 1642248000
```

## Data Sources Integration

The backend should integrate with these data sources:

### ACLED (Armed Conflict Location & Event Data Project)
- **API**: https://developer.acleddata.com/
- **Data**: Conflict events, fatalities, locations
- **Rate Limit**: 1000 requests/day

### GDELT (Global Database of Events, Language, and Tone)
- **API**: https://www.gdeltproject.org/data.html
- **Data**: Global events, news coverage, sentiment
- **Rate Limit**: 1000 requests/day

### ReliefWeb
- **API**: https://reliefweb.int/api
- **Data**: Humanitarian reports, appeals, updates
- **Rate Limit**: 1000 requests/day

### World Bank Open Data
- **API**: https://datahelpdesk.worldbank.org/knowledgebase/articles/898581
- **Data**: Economic indicators, development data
- **Rate Limit**: 1000 requests/day

## LLM Integration

### Ollama Configuration
- **Base URL**: `http://localhost:11434`
- **Model**: `llama2` (or `llama3` if available)
- **Context Window**: 4096 tokens
- **Temperature**: 0.7

### RAG Pipeline
1. **Chunking**: Split documents into 512-token chunks
2. **Embedding**: Generate embeddings using sentence-transformers
3. **Storage**: Store in ChromaDB with metadata
4. **Retrieval**: Retrieve top-k relevant chunks
5. **Generation**: Generate report with Ollama using retrieved context

## Implementation Notes

1. **Async Processing**: Report generation should be asynchronous
2. **Progress Tracking**: Implement real-time progress updates
3. **Error Handling**: Graceful fallbacks for API failures
4. **Caching**: Cache frequently accessed data
5. **Logging**: Comprehensive logging for debugging
6. **Monitoring**: Health checks and metrics

## Testing

The frontend will test the backend with:
1. **Mock Mode**: `USE_MOCK_DATA=true` (current implementation)
2. **Real Mode**: `USE_MOCK_DATA=false` (backend integration)
3. **Error Handling**: Test various error scenarios
4. **Performance**: Test with long-running operations

## Deployment

The backend should be deployable as:
1. **Docker Container**: With all dependencies
2. **Local Development**: With Python virtual environment
3. **Cloud Deployment**: AWS/GCP/Azure compatible

## Security Considerations

1. **Input Validation**: Validate all inputs
2. **Rate Limiting**: Implement rate limiting
3. **Error Messages**: Don't expose sensitive information
4. **API Keys**: Secure storage of API keys
5. **CORS**: Configure CORS for frontend access
