# Tests for Sentiment Analyzer API

import sys
import os

# Add parent directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_positive_sentiment():
    """Test for positive text"""
    response = client.post(
        "/analyze",
        json={"text": "This movie was fantastic! I loved it."}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "positive"


def test_negative_sentiment():
    """Test for negative text"""
    response = client.post(
        "/analyze",
        json={"text": "Terrible experience. Very bad."}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "negative"

def test_neutral_sentiment():
    """Test for neutral text"""
    response = client.post(
        "/analyze",
        json={"text": "Product is delivered as stated in the seller's description."}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "neutral"

def test_empty_text():
    """Test for empty string"""
    response = client.post(
        "/analyze",
        json={"text": ""}
    )
    assert response.status_code == 400