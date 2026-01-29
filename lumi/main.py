import sys
import threading
import time
from dotenv import load_dotenv

# Load env vars from the legacy path which user is editing
load_dotenv(dotenv_path="e:\\LUMI AI\\JARVIS-AI-Assistant-main\\.env") 

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QObject, pyqtSignal, QTimer

# Import components
from lumi.ui.splash import CinematicSplash
from lumi.ui.desktop_ui import LUMIUI
from lumi.core.orchestrator import Orchestrator
from lumi.core.wake_word import WakeWordListener
from lumi.voice.stt import SpeechToText
from lumi.voice.tts import TextToSpeech
from lumi.ai.router import AIRouter
from lumi.tool_manager import ToolManager 

# Signal Bridge to update UI from background threads
class SignalBridge(QObject):
    update_status = pyqtSignal(str)
    add_message = pyqtSignal(str, str)

from lumi.ui.login import LoginUI

class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.bridge = SignalBridge()
        
        # 1. Initialize Backend
        self.stt = SpeechToText()
        self.tts = TextToSpeech()
        self.router = AIRouter()
        try:
            self.wake_word = WakeWordListener(on_wake=self.on_wake)
        except:
            self.wake_word = None
        
        # 2. UI Instances
        self.splash = CinematicSplash()
        self.login_ui = LoginUI()
        self.ui = LUMIUI()
        
        # 3. Connect Signals
        self.bridge.update_status.connect(self.ui.update_status)
        self.bridge.add_message.connect(self.ui.add_message)
        
        self.ui.send_btn.clicked.connect(self.on_submit_text)
        self.ui.text_input.returnPressed.connect(self.on_submit_text)
        
        self.login_ui.login_successful.connect(self.on_login_success)

    def start(self):
        # Step 1: Show Splash
        self.splash.show()
        
        # Simulate load then show Login
        QTimer.singleShot(3000, self.show_login)
        
        sys.exit(self.app.exec())

    def show_login(self):
        self.splash.close()
        self.login_ui.show()

    def on_login_success(self):
        self.login_ui.close()
        self.ui.show()
        
        # Start Listeners
        if self.wake_word:
            threading.Thread(target=self.wake_word.start, daemon=True).start()

    def on_submit_text(self):
        text = self.ui.text_input.text()
        if text:
            self.ui.text_input.clear()
            self.process_command(text_input=text)

    def on_wake(self):
        """Called when wake word is detected."""
        self.bridge.update_status.emit("LISTENING")
        self.bridge.add_message.emit("System", "Wake Word Detected")
        
        # Play generic sound or speak
        # self.tts.speak_async("Yes?") 
        
        # Listen for command
        threading.Thread(target=self.process_voice_command, daemon=True).start()

    def process_voice_command(self):
        command = self.stt.listen()
        self.process_command(text_input=command)

    def process_command(self, text_input=None):
        """Handles the listening and processing flow."""
        command = text_input
        
        if command:
            self.bridge.add_message.emit("User", command)
            self.bridge.update_status.emit("PROCESSING")
            
            # Route to AI
            response = self.router.route_and_generate(command)
            
            self.bridge.update_status.emit("RESPONDING")
            self.bridge.add_message.emit("LUMI", response)
            
            # Speak Response
            self.tts.speak(response)
            
            self.bridge.update_status.emit("SLEEPING")
        else:
            self.bridge.update_status.emit("SLEEPING")
            self.bridge.add_message.emit("System", "No command heard")

if __name__ == "__main__":
    main = MainApp()
    main.start()
