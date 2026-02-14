import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'
import Header from './common/header/Header'
import Batch_analyzer from './pages/batch_analyzer/Batch_analyzer'
import Analyzer from './pages/analyzer/Analyzer'

function App() {

  return (
    <>
      <BrowserRouter>
        <Header />

        <Routes>
          <Route path="/" element={<Analyzer />} />
          <Route path="/batch-analyze" element={<Batch_analyzer />} />
        </Routes>

      </BrowserRouter>
    </>
  )
}

export default App
