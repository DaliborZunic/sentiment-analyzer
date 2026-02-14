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


def test_batch_analyze_multiple_texts():
    """Test batch analysis with multiple texts"""
    response = client.post(
        "/analyze/batch",
        json={
            "texts": [
                "This is amazing! I love it!",
                "Terrible product, very disappointed.",
                "The product arrived on time."
            ]
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert len(data["results"]) == 3
    assert data["results"][0]["sentiment"] == "positive"
    assert data["results"][1]["sentiment"] == "negative"
    assert data["results"][2]["sentiment"] == "neutral"


def test_batch_analyze_single_text():
    """Test batch analysis with single text"""
    response = client.post(
        "/analyze/batch",
        json={"texts": ["Great experience!"]}
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data["results"]) == 1
    assert data["results"][0]["sentiment"] == "positive"


def test_batch_analyze_empty_list():
    """Test batch analysis with empty list"""
    response = client.post(
        "/analyze/batch",
        json={"texts": []}
    )
    assert response.status_code == 400


def test_batch_analyze_with_empty_strings():
    """Test batch analysis with some empty strings"""
    response = client.post(
        "/analyze/batch",
        json={
            "texts": [
                "Great product!",
                "",
                "Awful experience."
            ]
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data["results"]) == 3
    assert data["results"][0]["sentiment"] == "positive"
    assert data["results"][1]["sentiment"] == "neutral"
    assert data["results"][1]["confidence"] == 0.0
    assert data["results"][2]["sentiment"] == "negative"