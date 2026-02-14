from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from app.models import SentimentRequest, SentimentResponse, BatchSentimentRequest, BatchSentimentResponse
from app.analyzer import SentimentAnalyzer

# Create FastAPI application
app = FastAPI(
    title="Sentiment Analyzer API",
    description="REST API for analyzing sentiment of English text",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize sentiment analyzer with error handling
try:
    sentiment_analyzer = SentimentAnalyzer()
except Exception as e:
    print(f"Failed to initialize VADER: {e}")
    sentiment_analyzer = None

@app.post("/analyze")
def analyze_sentiment(request: SentimentRequest):
    """
    Analyze sentiment of provided text.
    
    Returns sentiment (positive/negative/neutral) with confidence score.
    """
    # Check if analyzer initialized successfully
    if sentiment_analyzer is None:
        raise HTTPException(
            status_code=503,
            detail={"error": "Sentiment analyzer is not available", "status": 503}
        )
    
    # Check if text is empty
    if not request.text or request.text.strip() == "":
        raise HTTPException(
            status_code=400,
            detail={"error": "Text cannot be empty", "status": 400}
        )
    
    # Analyze sentiment
    result = sentiment_analyzer.analyze(request.text)
    
    # Return response
    return SentimentResponse(
        text=request.text,
        sentiment=result["sentiment"],
        confidence=result["confidence"]
    )

@app.post("/analyze/batch")
def analyze_batch(request: BatchSentimentRequest):
    """
    Analyze sentiment for multiple texts.
    
    Returns list of sentiment results for each text.
    """
    # Check if analyzer initialized successfully
    if sentiment_analyzer is None:
        raise HTTPException(
            status_code=503,
            detail={"error": "Sentiment analyzer is not available", "status": 503}
        )
    
    # Check if texts list is empty
    if not request.texts or len(request.texts) == 0:
        raise HTTPException(
            status_code=400,
            detail={"error": "Texts list cannot be empty", "status": 400}
        )
    
    # Use service to analyze batch
    batch_results = sentiment_analyzer.analyze_batch(request.texts)
    
    # Convert to response models
    results = [
        SentimentResponse(
            text=item["text"],
            sentiment=item["sentiment"],
            confidence=item["confidence"]
        )
        for item in batch_results
    ]
    
    # Return batch response
    return BatchSentimentResponse(results=results)