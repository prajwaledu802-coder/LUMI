import pyttsx3
import logging
import threading
import os
import requests

logger = logging.getLogger("TTS")

class TextToSpeech:
    def __init__(self, engine_id=None):
        self.engine = pyttsx3.init()
        self.set_voice(engine_id)
        
        # Configure standard settings
        self.engine.setProperty('rate', 170)
        self.engine.setProperty('volume', 1.0)
        
        self.elevenlabs_key = os.getenv("ELEVEN_API_KEY") # User said "11 large Germany" -> ElevenLabs
        self.use_elevenlabs = False
        if self.elevenlabs_key:
            logger.info("ElevenLabs API Key found. Using Neural Voice.")
            self.use_elevenlabs = True

    def set_voice(self, voice_id=None):
        voices = self.engine.getProperty('voices')
        if voice_id:
            try:
                self.engine.setProperty('voice', voice_id)
            except:
                pass
            return

        for voice in voices:
            if "Zira" in voice.name:
                self.engine.setProperty('voice', voice.id)
                return
        if voices:
            self.engine.setProperty('voice', voices[0].id)

    def speak(self, text):
        """Speaks text using ElevenLabs (if avail) or pyttsx3."""
        logger.info(f"Speaking: {text}")
        
        if self.use_elevenlabs:
            self.speak_elevenlabs(text)
        else:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception as e:
                logger.error(f"TTS Error: {e}")

    def speak_elevenlabs(self, text):
        try:
            # Simple direct API call to avoid complex lib dependency if not needed, 
            # or use the library if installed. Providing robust fallback.
            
            # Using standard 'Adam' or similar voice ID. 
            # Ideally config should specify voice_id.
            voice_id = "21m00Tcm4TlvDq8ikWAM" # Rachel
            
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": self.elevenlabs_key
            }
            data = {
                "text": text,
                "model_id": "eleven_monolingual_v1",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.5
                }
            }
            
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 200:
                with open("output.mp3", "wb") as f:
                    f.write(response.content)
                # Play it
                os.system("start output.mp3") # Windows specific
                # For non-blocking, we might want to use playsound or pygame
            else:
                logger.error(f"ElevenLabs Error: {response.text}")
                # Fallback
                self.engine.say(text)
                self.engine.runAndWait()
                
        except Exception as e:
            logger.error(f"ElevenLabs Exception: {e}")
            self.engine.say(text)
            self.engine.runAndWait()

    def speak_async(self, text):
        threading.Thread(target=self.speak, args=(text,), daemon=True).start()
