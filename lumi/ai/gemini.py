import google.generativeai as genai
import os
import logging

logger = logging.getLogger("GeminiAI")

class GeminiClient:
    def __init__(self, api_key=None, model_name="gemini-1.5-flash"):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            logger.warning("Gemini API Key missing")
            self.model = None
            return

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate_response(self, prompt):
        if not self.model:
            return "Gemini API key is missing."
        
        try:
            logger.info(f"Sending to Gemini: {prompt}")
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Gemini Error: {e}")
            return f"Error communicating with Gemini: {e}"
