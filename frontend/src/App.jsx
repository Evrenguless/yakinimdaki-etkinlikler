import { useEffect, useState } from 'react';

function App() {
  const [msg, setMsg] = useState('');

  useEffect(() => {
    fetch('http://localhost:4000/api/hello')
      .then(r => r.json())
      .then(d => setMsg(d.message));
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>Yakınımdaki Etkinlikler (Frontend)</h1>
      <p>Backend cevabı: {msg}</p>
    </div>
  );
}

export default App;
