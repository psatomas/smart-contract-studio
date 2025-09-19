import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Contracts from './components/Contracts'

function App() {
  const [count, setCount] = useState(0)
  const [message, setMessage] = useState('') // new state for backend message

  useEffect(() => {
    fetch('http://localhost:8000/api/hello/')
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch((err) => console.error('Error fetching backend:', err))
  }, [])

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>

      {/* New backend message section */}
      <div className="card">
        <h2>Django backend says:</h2>
        <p>{message || 'Loading...'}</p>
      </div>

      {/* Contracts component */}
      <Contracts />

      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
