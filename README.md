# LUMI AI Assistant

**LUMI** is a professional, hybrid AI assistant built with Python. It features a modern, futuristic UI, voice interaction (STT/TTS), and an intelligent brain powered by Google Gemini and OpenAI GPT-4.

## Features
- **Hybrid AI Brain**: Automatically routes tasks to the best model (Gemini for chat/search, GPT for coding).
- **Voice Interaction**: Wake word ("Lumi") detection and natural Neural TTS (ElevenLabs / Microsoft Zira).
- **Core Tools**:
  - **Browser Control**: Open websites, search Google.
  - **System Control**: Volume, lock screen (expandable).
  - **Weather**: Real-time forecasts via OpenMeteo.
- **Modern UI**:
  - Cinematic Splash Screen.
  - Dark Mode "Glassmorphism" Dashboard.
  - Animated Status Orb.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/prajwaledu802-coder/LUMI.git
    cd LUMI
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: For voice support on Windows, you may need to install `pyaudio` via `pipwin` or Visual Studio Build Tools.*

## Security & Configuration 🔒

**IMPORTANT**: This project is configured to keep your API keys safe. **DO NOT** commit your keys to GitHub.

1.  **Project Settings**:
    - The main configuration is in `lumi/config/settings.yaml`.
    - Note that `api_keys` are set to empty strings by default for safety.

2.  **Add Your Keys (The Safe Way)**:
    - Create a file named `.env` or `settings.local.yaml` in the root directory.
    - Add your keys there:
      ```
      GEMINI_API_KEY=your_key_here
      OPENAI_API_KEY=your_key_here
      ELEVEN_API_KEY=your_key_here
      PICOVOICE_API_KEY=your_key_here
      ```
    - These files are already in `.gitignore` and will not be uploaded.

3.  **Run the application**:
    ```bash
    run_lumi.bat
    ```

## Architecture
- `lumi/core`: System orchestrator, wake word, memory.
- `lumi/ai`: AI routing logic (Gemini/GPT).
- `lumi/ui`: PyQt6-based user interface.
- `lumi/voice`: TTS and STT modules.
- `lumi/tools`: Interactions with the OS and Web.

## License
MIT
