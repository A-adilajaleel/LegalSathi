import React from 'react'
import { VscLaw } from "react-icons/vsc";
const Hero = () => {
  return (
    <div className="bg-blue-700 text-white text-center py-16 px-4">
      <h1 className="text-4xl font-bold mb-4">  <VscLaw />  LegalSathi AI</h1>
      <p className="text-xl mb-2">Upload any legal document</p>
      <p className="text-lg text-blue-200">
        Get instant explanation in simple English, Hindi or Malayalam
      </p>
    </div>
  )
}

export default Hero
