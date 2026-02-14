from pydantic import BaseModel


class SentimentRequest(BaseModel):
    """Request model for sentiment analysis"""
    text: str


class SentimentResponse(BaseModel):
    """Response model for sentiment analysis"""
    text: str
    sentiment: str
    confidence: float