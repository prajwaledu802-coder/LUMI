try:
    import speech_recognition as sr
except ImportError:
    sr = None
    print("SpeechRecognition not installed.")
import logging

logger = logging.getLogger("STT")

class SpeechToText:
    def __init__(self, engine="google"):
        self.engine = engine
        self.recognizer = sr.Recognizer()
        try:
            self.microphone = sr.Microphone()
        except Exception as e:
            self.microphone = None
            logger.error(f"Microphone not available: {e}")

    def listen(self, prompt_text=None):
        """Listens for a command and returns text."""
        if not self.microphone:
            logger.error("No microphone detected. Cannot listen.")
            return None

        try:
            with self.microphone as source:
                if prompt_text:
                    logger.info(f"Listening... ({prompt_text})")
                else:
                    logger.info("Listening...")
                
                # Fast adjustment
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
            text = self.recognizer.recognize_google(audio) # Defaulting to google for now
            logger.info(f"Heard: {text}")
            return text
            
        except sr.WaitTimeoutError:
            logger.warning("Listening timed out.")
            return None
        except sr.UnknownValueError:
            logger.warning("Could not understand audio.")
            return None
        except Exception as e:
            logger.error(f"STT Error: {e}")
            return None
