import os
import base64
from groq import Groq
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import PyPDF2

client = Groq(api_key=settings.GROQ_API_KEY)

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def get_prompt(language):
    prompts = {
        'english': """You are LegalSathi AI. Analyze this legal document and explain it in very simple English that a common person can understand. 
        Structure your response as:
        1. What is this document?
        2. Key points (simple bullets)
        3. Important things to note
        4. Any risks or warnings""",
        'hindi': """आप LegalSathi AI हैं। इस legal document को analyze करें और बहुत सरल हिंदी में समझाएं।
        1. यह document क्या है?
        2. मुख्य बातें
        3. जरूरी बातें
        4. कोई खतरा या चेतावनी""",
        'malayalam': """നിങ്ങൾ LegalSathi AI ആണ്. ഈ legal document സാധാരണ Malayalam-ൽ വിശദീകരിക്കൂ.
        1. ഈ document എന്താണ്?
        2. പ്രധാന കാര്യങ്ങൾ
        3. ശ്രദ്ധിക്കേണ്ട കാര്യങ്ങൾ
        4. Risks അല്ലെങ്കിൽ warnings"""
    }
    return prompts.get(language, prompts['english'])

@api_view(['POST'])
def analyze_document(request):
    print("=== REQUEST RECEIVED ===")
    try:
        file = request.FILES.get('file')
        language = request.data.get('language', 'english')

        print("FILE:", file)
        print("LANGUAGE:", language)

        if not file:
            return Response({'error': 'No file uploaded'}, status=400)

        prompt = get_prompt(language)

        # PDF or Image — text extract ചെയ്യുന്നു
        if file.name.lower().endswith('.pdf'):
            print("Processing PDF...")
            text = extract_text_from_pdf(file)
            if not text.strip():
                return Response({'error': 'Could not extract text from PDF'}, status=400)
        else:
            print("Processing Image...")
            # Image-നെ base64 ആക്കി text ആയി treat ചെയ്യുന്നു
            image_bytes = file.read()
            image_base64 = base64.b64encode(image_bytes).decode('utf-8')
            text = f"[This is an image document - base64: {image_base64[:100]}... Please analyze as a legal document image]"

        full_prompt = f"{prompt}\n\nDocument content:\n{text}"

        print("Calling Groq API...")
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": full_prompt
                }
            ],
            max_tokens=2000,
            temperature=0.3
        )

        summary = response.choices[0].message.content
        print("SUCCESS!")
        return Response({'summary': summary})

    except Exception as e:
        print("ERROR DETAILS:", str(e))
        import traceback
        traceback.print_exc()
        return Response({'error': str(e)}, status=500)