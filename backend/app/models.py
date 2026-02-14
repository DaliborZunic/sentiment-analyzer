from pydantic import BaseModel
from typing import List


class SentimentRequest(BaseModel):
    """Request model for sentiment analysis"""
    text: str


class SentimentResponse(BaseModel):
    """Response model for sentiment analysis"""
    text: str
    sentiment: str
    confidence: float


class BatchSentimentRequest(BaseModel):
    """Request model for batch sentiment analysis"""
    texts: List[str]


class BatchSentimentResponse(BaseModel):
    """Response model for batch sentiment analysis"""
    results: List[SentimentResponse]