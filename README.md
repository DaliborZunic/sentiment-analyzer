# Sentiment Analyzer

A REST API + React frontend for analyzing sentiment of English text using VADER (Valence Aware Dictionary and sEntiment Reasoner).

## Features

- Analyzes text sentiment as positive, negative, or neutral
- Provides confidence scores for predictions
- Fast and lightweight
- Interactive API documentation with Swagger UI
- Comprehensive test suite

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Node.js and npm (for frontend)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/DaliborZunic/sentiment-analyzer.git
```

### 2. Create a virtual environment for API

**Windows:**
```bash
cd sentiment-analyzer/backend
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
cd sentiment-analyzer/backend
python3 -m venv .venv
source .venv/bin/activate
```

You should see `(.venv)` appear in your terminal prompt, indicating the virtual environment is active.

### 3. Install dependencies for API

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

## Running the Frontend

The project includes a React TypeScript frontend built with Vite.

### 1. Navigate to the frontend directory

From the project root:

```bash
cd frontend
```

### 2. Install dependencies for frontend

```bash
npm install
```

### 3. Start the development server for frontend

```bash
npm run dev
```

The frontend will run on http://localhost:5173

### 4. Using the application

1. Make sure the backend server is running (see "Running the Server" section above)
2. Open http://localhost:5173 in your browser
3. Enter text in the textarea
4. Click "Go!" to analyze the sentiment
5. View the results below showing sentiment and confidence score
6. Try the batch analyzer also!

### Stop the frontend server

Press `Ctrl+C` in the terminal where the frontend is running.
