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
        'english': """You are LegalSathi AI. Your job is to help common people understand legal documents.

Explain this document as if you're talking to a farmer, student, or common person who has never read a legal document before. Use very simple everyday words. No legal jargon at all.

Format your response exactly like this:

📄 **What is this document?**
(One simple sentence — what is this about?)

👥 **Who is involved?**
(Names and roles in simple words)

✅ **What does this mean for you?**
(Simple bullet points — what you get, what you must do)

⚠️ **Important warnings before signing:**
(What to be careful about)""",

        'hindi': """आप LegalSathi AI हैं। आपका काम है आम लोगों को legal documents समझाना।

इस document को ऐसे समझाएं जैसे आप एक किसान, student, या आम इंसान से बात कर रहे हैं जिसने कभी legal document नहीं पढ़ा। बिल्कुल simple भाषा में।

इस format में जवाब दें:

📄 **यह document क्या है?**
(एक simple sentence में)

👥 **इसमें कौन-कौन है?**
(नाम और role simple में)

✅ **आपके लिए इसका मतलब क्या है?**
(Simple points — आपको क्या मिलेगा, क्या करना होगा)

⚠️ **Sign करने से पहले ध्यान दें:**
(क्या सावधानी रखें)""",

        'malayalam': """നിങ്ങൾ LegalSathi AI ആണ്. നിങ്ങളുടെ ജോലി സാധാരണക്കാർക്ക് legal documents മനസ്സിലാക്കി കൊടുക്കുക എന്നതാണ്.

ഈ document ഒരിക്കലും legal document വായിച്ചിട്ടില്ലാത്ത ഒരു കർഷകന്, student, അല്ലെങ്കിൽ സാധാരണ മനുഷ്യന് മനസ്സിലാകുന്ന രീതിയിൽ explain ചെയ്യൂ. Legal terms ഒരിക്കലും ഉപയോഗിക്കരുത്. നാട്ടുഭാഷയിൽ സംസാരിക്കുന്നത് പോലെ explain ചെയ്യൂ.

ഈ format-ൽ മറുപടി നൽകൂ:

📄 **ഈ document എന്താണ്?**
(ഒരു simple sentence — ഇത് എന്തിനെ കുറിച്ചാണ്?)

👥 **ആരൊക്കെ ഉണ്ട്?**
(പേരുകളും roles-ഉം simple ആയി)

✅ **നിനക്ക് ഇതിന്റെ അർത്ഥം എന്താണ്?**
(Simple points — നിനക്ക് എന്ത് കിട്ടും, നീ എന്ത് ചെയ്യണം)

⚠️ **Sign ചെയ്യുന്നതിന് മുമ്പ് ശ്രദ്ധിക്കൂ:**
(എന്തൊക്കെ careful ആയി നോക്കണം)"""
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

        if file.name.lower().endswith('.pdf'):
            print("Processing PDF...")
            text = extract_text_from_pdf(file)
            if not text.strip():
                return Response({'error': 'Could not extract text from PDF'}, status=400)
            text = text[:6000]
        else:
            print("Processing Image...")
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