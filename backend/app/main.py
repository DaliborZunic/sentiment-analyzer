import uvicorn
from fastapi import FastAPI, HTTPException
from models import SentimentRequest, SentimentResponse
from analyzer import SentimentAnalyzer

# Create FastAPI application
app = FastAPI(
    title="Sentiment Analyzer API",
    description="REST API for analyzing sentiment of English text",
    version="1.0.0"
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)