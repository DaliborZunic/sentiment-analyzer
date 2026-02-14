# Sentiment Analyzer API

A REST API for analyzing sentiment of English text using VADER (Valence Aware Dictionary and sEntiment Reasoner).

## Features

- Analyzes text sentiment as positive, negative, or neutral
- Provides confidence scores for predictions
- Fast and lightweight
- Interactive API documentation with Swagger UI
- Comprehensive test suite

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd sentiment-analyzer/backend
```

### 2. Create a virtual environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

You should see `(.venv)` appear in your terminal prompt, indicating the virtual environment is active.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages including:
- FastAPI - Web framework
- Uvicorn - ASGI server
- Pydantic - Data validation
- vaderSentiment - Sentiment analysis
- pytest - Testing framework

## Running the Server

### Start the development server

From the `backend` directory with your virtual environment activated:

```bash
uvicorn app.main:app --reload
```

The `--reload` flag enables auto-reload when you make code changes (recommended for development).

### Access the API

Once the server is running, you can access:

- **Interactive API Documentation (Swagger UI)**: http://127.0.0.1:8000/docs
- **Alternative API Documentation (ReDoc)**: http://127.0.0.1:8000/redoc

### Stop the server

Press `Ctrl+C` in the terminal where the server is running.

## Using the API

### Interactive Documentation (Recommended)

1. Open http://127.0.0.1:8000/docs in your browser
2. Click on the `/analyze` endpoint
3. Click "Try it out"
4. Enter your text in the request body:
   ```json
   {
     "text": "I love this product! It works great!"
   }
   ```
5. Click "Execute"
6. View the response below

### Example with curl

```bash
curl -X POST http://127.0.0.1:8000/analyze \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"I love this product! It works great!\"}"
```

## Running Tests

### Run all tests

From the `backend` directory with your virtual environment activated:

```bash
pytest -v
```

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI application and endpoints
│   ├── models.py         # Pydantic models for request/response
│   └── analyzer.py       # Sentiment analysis logic
├── tests/
│   ├── __init__.py
│   └── test_api.py       # API tests
├── requirements.txt      # Python dependencies
├── .venv/               # Virtual environment (created by you)
└── README.md            # This file
```

