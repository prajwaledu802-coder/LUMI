try:
    import pvporcupine
except ImportError:
    pvporcupine = None
    print("Picovoice (pvporcupine) not installed.")
import struct
try:
    import pyaudio
except ImportError:
    pyaudio = None
    print("PyAudio not installed. Microphone access will be disabled.")
import logging
import os

logger = logging.getLogger("WakeWord")

class WakeWordListener:
    def __init__(self, on_wake=None):
        self.on_wake = on_wake
        self.access_key = os.getenv("PICOVOICE_API_KEY") # "Pico voise" key
        self.porcupine = None
        self.pa = None
        self.audio_stream = None
        self.is_listening = False

        if not self.access_key:
            logger.warning("Picovoice API Key missing. Wake Word disabled.")
            return

        try:
            self.porcupine = pvporcupine.create(access_key=self.access_key, keywords=["jarvis", "picovoice"]) # Default keywords or specific file
            # Note: "Lumi" custom model requires a .ppn file. For now using "Jarvis" or generic since custom requires training file.
            # Assuming user might have key but maybe not model yet. Using 'porcupine' (default) for test.
        except Exception as e:
            logger.error(f"Picovoice Init Error: {e}")

    def start(self):
        if not self.porcupine:
            return
            
        logger.info("Starting Wake Word Listener (Picovoice)...")
        self.is_listening = True
        
        try:
            self.pa = pyaudio.PyAudio()
            self.audio_stream = self.pa.open(
                rate=self.porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=self.porcupine.frame_length
            )

            while self.is_listening:
                pcm = self.audio_stream.read(self.porcupine.frame_length)
                pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)

                keyword_index = self.porcupine.process(pcm)
                if keyword_index >= 0:
                    logger.info("Wake Word Detected!")
                    if self.on_wake:
                        self.on_wake()

        except Exception as e:
            logger.error(f"Wake Word Loop Error: {e}")
        finally:
            if self.porcupine:
                self.porcupine.delete()
            if self.audio_stream:
                self.audio_stream.close()
            if self.pa:
                self.pa.terminate()

    def stop(self):
        self.is_listening = False
