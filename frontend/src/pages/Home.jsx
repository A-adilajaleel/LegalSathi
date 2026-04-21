import React, { useState } from 'react'
import UploadSection from '../components/UploadSection'
import ResultSection from '../components/ResultSection'
import Hero from '../components/Hero'


const Home = () => {
     const [result, setResult] = useState(null)

  return (
    <div>
      <Hero />
      <UploadSection setResult={setResult} />
      {result && <ResultSection result={result} />}
    </div>
  )
}

export default Home
