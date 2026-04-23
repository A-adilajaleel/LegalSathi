import { useState } from 'react'
import axios from 'axios'

function UploadSection({ setResult }) {
  const [file, setFile] = useState(null)
  const [language, setLanguage] = useState('english')
  const [loading, setLoading] = useState(false)

  const handleUpload = async () => {
    if (!file) return alert('Please select a file!')
    setLoading(true)

    const formData = new FormData()
    formData.append('file', file)
    formData.append('language', language)

    try {
      const res = await axios.post('https://legalsathi-backend.onrender.com/api/analyze/', formData)
      setResult(res.data)
    } catch (err) {
      alert('Something went wrong!')
    }
    setLoading(false)
  }

  return (
    <div className="max-w-2xl mx-auto my-10 p-6 bg-white rounded-2xl shadow-lg">
      <h2 className="text-xl font-semibold text-gray-700 mb-4">
        <img  src="https://cdn-icons-png.flaticon.com/128/10848/10848828.png"
    width="24"
    alt="upload"/> 
    Upload Your Document
      </h2>

      <input
        type="file"
        accept=".pdf,.png,.jpg,.jpeg"
        onChange={(e) => setFile(e.target.files[0])}
        className="w-full border-2 border-dashed border-blue-300 rounded-xl p-4 mb-4 cursor-pointer"
      />

      <select
        value={language}
        onChange={(e) => setLanguage(e.target.value)}
        className="w-full border border-gray-300 rounded-xl p-3 mb-4"
      >
        <option value="english">English</option>
        <option value="hindi">Hindi</option>
        <option value="malayalam">Malayalam</option>
      </select>

     <button
  onClick={handleUpload}
  disabled={loading}
  className="w-full bg-blue-700 text-white py-3 rounded-xl font-semibold hover:bg-blue-800 transition flex items-center justify-center gap-2"
>
  {loading ? (
    <>
      <img
        src="https://cdn-icons-png.flaticon.com/128/9342/9342527.png"
        width="20"
        alt="loading"
      />
      Analyzing...
    </>
  ) : (
    <>
      <img
        src="https://cdn-icons-png.flaticon.com/128/12397/12397666.png"
        width="20"
        alt="analyze"
      />
      Analyze Document
    </>
  )}
</button>
    </div>
  )
}

export default UploadSection