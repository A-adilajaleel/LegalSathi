import React from 'react'
import ReactMarkdown from 'react-markdown'

const ResultSection = ({result}) => {
  return (
    <div className="max-w-2xl mx-auto my-6 p-6 bg-green-50 rounded-2xl shadow-lg">
      <h2 className="text-xl font-semibold text-green-700 mb-4 flex items-center gap-2">
        <img
          src="https://cdn-icons-png.flaticon.com/128/16318/16318642.png"
          width="24"
          alt="summary"
        />
        Document Summary
      </h2>
      <div className="text-gray-700 leading-relaxed prose prose-sm max-w-none">
        <ReactMarkdown>{result.summary}</ReactMarkdown>
      </div>
    </div>
  )
}

export default ResultSection