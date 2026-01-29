import logging
from lumi.ai.gemini import GeminiClient
from lumi.ai.gpt import GPTClient

logger = logging.getLogger("AIRouter")

class AIRouter:
    def __init__(self):
        self.gemini = GeminiClient()
        self.gpt = GPTClient()

    def route_and_generate(self, prompt):
        """Decides which AI to use based on the prompt."""
        prompt_lower = prompt.lower()
        
        # Routing Logic
        if "code" in prompt_lower or "python" in prompt_lower or "function" in prompt_lower or "script" in prompt_lower or "debug" in prompt_lower:
            logger.info("Routing to: GPT (Coding Task)")
            # Prefer GPT for coding, fallback to Gemini if GPT not available
            if self.gpt.client:
                return self.gpt.generate_response(prompt)
            else:
                logger.warning("GPT not available, falling back to Gemini")
                return self.gemini.generate_response(prompt)
        
        elif "search" in prompt_lower or "find" in prompt_lower or "news" in prompt_lower:
             logger.info("Routing to: Gemini (Search/Knowledge Task)")
             return self.gemini.generate_response(prompt)

        else:
             logger.info("Routing to: Gemini (General Conversation)")
             return self.gemini.generate_response(prompt)
