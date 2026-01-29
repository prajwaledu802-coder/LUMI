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

3.  Configure API Keys:
    - Create a `.env` file in the root directory.
    - Add your keys:
      ```
      GEMINI_API_KEY=your_key
      OPENAI_API_KEY=your_key
      ELEVEN_API_KEY=your_key
      PICOVOICE_API_KEY=your_key
      ```

4.  Run the application:
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
