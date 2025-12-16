import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def get_gemini_model():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file")

    genai.configure(api_key=api_key)

    # ✅ Correct model name (NO "models/")
    return genai.GenerativeModel("models/gemini-2.5-flash")


def generate_ai_response(prompt: str) -> str:
    model = get_gemini_model()
    response = model.generate_content(prompt)
    return response.text.strip()