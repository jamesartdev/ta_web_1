import { useEffect, useState } from 'react'

export default function App() {
  const [message, setMessage] = useState('กำลังเรียก backend...')

  useEffect(() => {
    // /api/ จะถูก Vite proxy ส่งต่อไปที่ http://backend:8000/
    fetch('/api/')
      .then((res) => res.json())
      .then((data) => setMessage(JSON.stringify(data)))
      .catch(() => setMessage('เรียก backend ไม่สำเร็จ'))
  }, [])

  return (
    <div style={{ fontFamily: 'sans-serif', padding: 24 }}>
      <h1>Frontend ทำงานแล้ว</h1>
      <p>ผลจาก backend: {message}</p>
    </div>
  )
}
