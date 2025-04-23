import React from 'react';
import logo from './logo.svg';
import './App.css';

// frontend/src/App.tsx
function App() {
  const handleClick = async () => {
    const res = await fetch("http://localhost:8000/hello");
    const data = await res.json();
    alert(data.message);
  };

  return (
    <div>
      <h1>Hello from React</h1>
      <button onClick={handleClick}>Call API</button>
    </div>
  );
}
export default App;
