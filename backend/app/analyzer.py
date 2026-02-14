from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from typing import List


class SentimentAnalyzer:
    """Sentiment analyzer using VADER"""
    
    def __init__(self):
        """Initialize VADER sentiment analyzer"""
        self.analyzer = SentimentIntensityAnalyzer()
    
    def analyze(self, text: str) -> dict:
        """
        Analyze sentiment of the given text.
        
        Returns dictionary with sentiment and confidence score.
        """
        # Get VADER scores
        scores = self.analyzer.polarity_scores(text)
        
        # Get compound score (ranges from -1 to 1)
        compound = scores['compound']
        
        # Determine sentiment based on compound score
        if compound >= 0.05:
            sentiment = "positive"
            confidence = scores['pos']
        elif compound <= -0.05:
            sentiment = "negative"
            confidence = scores['neg']
        else:
            sentiment = "neutral"
            confidence = scores['neu']
        
        return {
            "sentiment": sentiment,
            "confidence": round(confidence, 2)
        }
    
    def analyze_batch(self, texts: List[str]) -> List[dict]:
        """
        Analyze sentiment for multiple texts.
        
        Returns list of dictionaries with sentiment and confidence for each text.
        """
        results = []
        
        for text in texts:
            # Handle empty text
            if not text or text.strip() == "":
                results.append({
                    "text": text,
                    "sentiment": "neutral",
                    "confidence": 0.0
                })
                continue
            
            # Analyze sentiment
            result = self.analyze(text)
            results.append({
                "text": text,
                "sentiment": result["sentiment"],
                "confidence": result["confidence"]
            })
        
        return results
    
    