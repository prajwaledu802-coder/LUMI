import openai
import os
import logging

logger = logging.getLogger("GPTAI")

class GPTClient:
    def __init__(self, api_key=None, model_name="gpt-4o"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            logger.warning("OpenAI API Key missing")
            self.client = None
            return

        self.client = openai.OpenAI(api_key=self.api_key)
        self.model_name = model_name

    def generate_response(self, prompt):
        if not self.client:
            return "OpenAI API key is missing."
        
        try:
            logger.info(f"Sending to GPT: {prompt}")
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"GPT Error: {e}")
            return f"Error communicating with GPT: {e}"
