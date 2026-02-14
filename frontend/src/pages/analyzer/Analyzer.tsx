import { useState } from 'react'
import './Analyzer.css'

interface SentimentResult {
  text: string
  sentiment: 'positive' | 'negative' | 'neutral'
  confidence: number
}

const Analyzer = () => {
  const [text, setText] = useState('')
  const [result, setResult] = useState<SentimentResult | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const analyzeSentiment = async () => {
    if (!text.trim()) {
      setError('Please enter some text')
      return
    }

    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const response = await fetch('http://localhost:8000/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text })
      })

      if (!response.ok) {
        throw new Error('Failed to analyze sentiment')
      }

      const data: SentimentResult = await response.json()
      setResult(data)
      setText('')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="analyzer-wrapper">
      <span className="intro-text">
        Please, input some text and click "Go!" to evaluate its sentiment
      </span>
      <div className="request-wrapper">
        <textarea 
          className="text-input"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter your text here..."
        />
        <div 
          className={`go-button ${loading ? 'loading' : ''}`}
          onClick={analyzeSentiment}
        >
          {loading ? 'Analyzing...' : 'Go!'}
        </div>
      </div>

      {error && (
        <div className="error-message">
          {error}
        </div>
      )}

      {result && (
        <div className="result-wrapper">
          <h3>Result:</h3>
          <div className="analyzed-text">
            "{result.text}"
          </div>
          <div className="sentiment-label">
            Sentiment: <span className={`sentiment-value ${result.sentiment}`}>
              {result.sentiment.toUpperCase()}
            </span>
          </div>
          <div className="confidence-score">
            Confidence: {(result.confidence * 100).toFixed(1)}%
          </div>
        </div>
      )}
    </div>
  )
}

export default Analyzer