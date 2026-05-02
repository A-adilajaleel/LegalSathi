# ⚖️ LegalSathi AI

A multilingual AI system that simplifies complex legal documents from PDFs and images using LLMs, OCR, and a translation pipeline.

---

## 🌐 Live Demo
👉 https://legal-sathi-eight.vercel.app/

---

## 🔍 Problem

Legal documents are often:
- Difficult to understand due to complex language
- Not accessible to non-English speakers
- Dependent on expensive legal consultation

This creates a major barrier to **access to justice**.

---

## 💡 Solution

LegalSathi enables users to:
1. Upload a legal document (PDF or image)
2. Extract and understand its content using AI
3. Receive a simplified explanation in:
   - English
   - Hindi
   - Malayalam

---

## ⚙️ System Architecture


User Upload (PDF/Image)
↓
OCR (Text Extraction)
↓
LLM Processing (LLaMA 3 via Groq)
↓
Legal Simplification
↓
Translation Pipeline
↓
Multilingual Output


---

## 🔄 Translation Pipeline

The system follows a structured pipeline:
1. Extract raw legal text from input
2. Convert complex legal language → simple English using LLM
3. Translate simplified output into Hindi and Malayalam

---

## 🚀 Features

- 📄 Upload PDF or scanned legal documents
- 🤖 AI-powered explanation using Groq (LLaMA 3.3 70B)
- 🌐 Multilingual output (English, Hindi, Malayalam)
- 🔒 Privacy-first: documents are not stored
- ⚡ Fast response generation

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React + Vite + Tailwind CSS |
| Backend | Django + Django REST Framework |
| AI | Groq API (LLaMA 3.3 70B) |
| OCR | (Mention tool if used, e.g. Tesseract) |
| Languages | English, Hindi, Malayalam |

---

## 📸 Screenshots

### Home Page
![Home](assets/home.png)

### Result Page
![Result](assets/result.png)

---

## ⚠️ Limitations & Risks

- AI may generate incorrect or incomplete legal interpretations
- Outputs should not be treated as professional legal advice
- Risk of hallucination in LLM responses
- Requires human/legal expert verification for critical use

---

## 🌍 Impact

LegalSathi aims to:
- Improve access to legal information
- Reduce language barriers in law
- Empower users without legal background

---

## 👨‍💻 Author

Adila Jaleel — Full Stack Developer
