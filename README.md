# 🔵 LUMI AI Assistant

**LUMI** is a professional, hybrid AI assistant built with Python. It features a modern, futuristic UI, voice interaction (STT/TTS), and an intelligent brain powered by Google Gemini and OpenAI GPT-4.



## ✨ Features

### 🧠 Hybrid AI Brain
- **Smart Routing**: Automatically routes tasks to the best model.
  - **Gemini**: For general conversation, creative writing, and search.
  - **GPT-4**: For complex coding and reasoning tasks.

### 🎙️ Voice Interaction
- **Wake Word**: "Lumi" or "Hey Lumi" (powered by Picovoice).
- **Neural TTS**: High-quality voice using **ElevenLabs** (with offline fallback to Microsoft Zira).
- **Resilient**: "Deaf Mode" support if microphone hardware is missing.

### 💻 Modern UI
- **Cinematic Splash Screen**: "Intelligence Architecture Initializing" sequence.
- **Glassmorphism Dashboard**: Frameless, translucent dark mode interface.
- **Secure Login**: Access terminal style login screen.
- **Web Interface**: Run LUMI in your browser via Streamlit.

### 🛠️ Core Tools
- **Browser**: Open websites and perform Google searches.
- **System**: Control volume, screen lock, and system power.
- **Weather**: Real-time forecasts via OpenMeteo (Pandas integrated).

---

## 🚀 Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/prajwaledu802-coder/LUMI.git
    cd LUMI
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    > **Note**: For voice support on Windows, you might need `pipwin install pyaudio` if the standard install fails.

3.  **Run the application**:
    - **Desktop App**:
      ```bash
      run_lumi.bat
      ```
    - **Web Interface (Chrome)**:
      ```bash
      streamlit run web_app.py
      ```

---

## 🔒 Security & Configuration

**IMPORTANT**: This project is configured to keep your API keys safe. **DO NOT** commit your keys to GitHub.

1.  **Project Settings**:
    - The main configuration is in `lumi/config/settings.yaml`.
    - `api_keys` are set to empty strings by default for safety.

2.  **Add Your Keys (The Safe Way)**:
    - Create a file named `.env` or `settings.local.yaml` in the root directory.
    - Add your keys there:
      ```env
      GEMINI_API_KEY=your_key_here
      OPENAI_API_KEY=your_key_here
      ELEVEN_API_KEY=your_key_here
      PICOVOICE_API_KEY=your_key_here
      ```
    - These files are already in `.gitignore` and will not be uploaded.

---

## 📂 Architecture

| Module | Description |
| :--- | :--- |
| `lumi/core` | System orchestrator, wake word listener, memory management. |
| `lumi/ai` | AI routing logic (Gemini/GPT wrappers). |
| `lumi/ui` | PyQt6-based Desktop UI and Streamlit Web UI. |
| `lumi/voice` | Text-to-Speech (TTS) and Speech-to-Text (STT) modules. |
| `lumi/tools` | Interactions with the OS, Files, and Web. |

---

## 📄 License

This project is licensed under the MIT License.
