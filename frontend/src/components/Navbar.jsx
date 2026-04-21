import React from 'react'

const Navbar = () => {
  return (
    <nav className="bg-white shadow-md px-6 py-4 flex items-center justify-between">
      
      <div className="flex items-center gap-2">
        <img
          src="https://cdn-icons-png.flaticon.com/128/17197/17197218.png"
          width="28"
          alt="Legal Sathi"
        />
        <span className="text-xl font-bold text-blue-700">
          LegalSathi
        </span>
      </div>

      <div className="text-sm text-gray-500">
        Your Legal Document Assistant
      </div>

    </nav>
  )
}

export default Navbar