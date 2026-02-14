import { useState } from 'react'
import './Batch_analyzer.css'

interface SentimentResult {
  text: string
  sentiment: 'positive' | 'negative' | 'neutral'
  confidence: number
}

interface BatchResult {
  results: SentimentResult[]
}

const BatchAnalyzer = () => {
  const [textInput, setTextInput] = useState('')
  const [results, setResults] = useState<SentimentResult[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const analyzeBatch = async () => {
    // Split text by newlines and filter empty lines
    const texts = textInput
      .split('\n')
      .map(line => line.trim())
      .filter(line => line.length > 0)

    if (texts.length === 0) {
      setError('Please enter at least one line of text')
      return
    }

    setLoading(true)
    setError(null)
    setResults([])

    try {
      const response = await fetch('http://localhost:8000/analyze/batch', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ texts })
      })

      if (!response.ok) {
        throw new Error('Failed to analyze texts')
      }

      const data: BatchResult = await response.json()
      setResults(data.results)
      setTextInput('')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="batch-analyzer-wrapper">
      <span className="intro-text">
        Enter multiple texts (one per line) and click "Analyze All!" to evaluate their sentiments
      </span>
      <div className="request-wrapper">
        <textarea 
          className="text-input"
          value={textInput}
          onChange={(e) => setTextInput(e.target.value)}
          placeholder="Enter texts here, one per line...&#10;Example:&#10;I love this product!&#10;This is terrible.&#10;It's okay, nothing special."
          rows={10}
        />
        <div 
          className={`go-button ${loading ? 'loading' : ''}`}
          onClick={analyzeBatch}
        >
          {loading ? 'Analyzing...' : 'Analyze All!'}
        </div>
      </div>

      {error && (
        <div className="error-message">
          {error}
        </div>
      )}

      {results.length > 0 && (
        <div className="results-wrapper">
          <h3 className="results-title">Results:</h3>
          <div className="results-list">
            {results.map((result, index) => (
              <div key={index} className="result-item">
                <div className="result-number">#{index + 1}</div>
                <div className="result-content">
                  <div className="analyzed-text">
                    "{result.text}"
                  </div>
                  <div className="result-details">
                    <span className={`sentiment-badge ${result.sentiment}`}>
                      {result.sentiment.toUpperCase()}
                    </span>
                    <span className="confidence-score">
                      {(result.confidence * 100).toFixed(1)}% confidence
                    </span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

export default BatchAnalyzer
