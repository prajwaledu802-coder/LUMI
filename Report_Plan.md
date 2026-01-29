# LUMI AI Assistant - Implementation Plan

## Goal Description
Rebuild the existing JARVIS prototype into LUMI, a professional, modular, hybrid AI assistant.
The goal is to move away from messy scripts to a clean, maintainable architecture with specific focus on:
- **Identity**: 'Lumi' wake word, friendly but professional personality.
- **Hybrid AI**: Routing between Gemini, GPT, and other models based on task.
- **Voice I/O**: High-quality STT and natural TTS (English, Hindi, etc.).
- **System Control**: Safe, permission-based control of browser, files, and windows.
- **UI**: Futuristic, minimal, dark mode, voice-reactive.

## User Review Required
> [!IMPORTANT]
> **API Keys**: I will need API keys for Gemini, OpenAI (GPT), and potentially others (e.g., Porcupine for wake word, ElevenLabs for TTS if desired, though I will start with standard libraries or free tiers if not provided).
>
> **Wake Word Engine**: For "Lumi" specifically, we might need a custom model (like Porcupine) or a generic energy/keyword detector if we want it completely offline/free without training. I will assume a standard library like `pvporcupine` (if key provided) or `SpeechRecognition` / `vosk` for now.
>
> **UI Framework**: For the "Desktop UI" and "3D Hologram", I plan to use `PyQt6` or `tkinter` with `customtkinter` for the modern look. For 3D, potentially `PyOpenGL` or a web-based UI wrapped in a window if we want advanced 3D. Given the "Desktop UI" requirement, `PyQt6` / `PySide6` is usually best for system integration.

## Proposed Changes

### Configuration & Core
#### [NEW] [settings.yaml](file:///e:/LUMI%20AI/lumi/config/settings.yaml)
- Centralized configuration for keys, preferences, and prompt templates.

#### [NEW] [wake_word.py](file:///e:/LUMI%20AI/lumi/core/wake_word.py)
- Logic to listen for "Lumi", "Hey Lumi".
- Uses a background thread to allow "Always listening".

#### [NEW] [orchestrator.py](file:///e:/LUMI%20AI/lumi/core/orchestrator.py)
- Main logic loop: Listen -> Understand -> Route -> Act -> Respond.

#### [NEW] [permissions.py](file:///e:/LUMI%20AI/lumi/core/permissions.py)
- Handles security levels (Read-only, System, Admin).
- Prompts for confirmation on dangerous actions.

#### [NEW] [memory.py](file:///e:/LUMI%20AI/lumi/core/memory.py)
- Short-term (session) and Long-term (JSON/SQLite) memory.

### AI & Intelligence
#### [NEW] [router.py](file:///e:/LUMI%20AI/lumi/ai/router.py)
- Logic to decide which model to use (Conversation -> Gemini, Coding -> GPT, etc.).

#### [NEW] [gemini.py](file:///e:/LUMI%20AI/lumi/ai/gemini.py)
- Google Gemini API wrapper.

#### [NEW] [gpt.py](file:///e:/LUMI%20AI/lumi/ai/gpt.py)
- OpenAI GPT API wrapper.

### Voice & Tools
#### [NEW] [stt.py](file:///e:/LUMI%20AI/lumi/voice/stt.py)
- Speech-to-Text implementation (Google Speech Recog / Whisper local).

#### [NEW] [tts.py](file:///e:/LUMI%20AI/lumi/voice/tts.py)
- Text-to-Speech implementation (pyttsx3 / EdgeTTS / ElevenLabs).

#### [NEW] [browser.py](file:///e:/LUMI%20AI/lumi/tools/browser.py)
- Selenium or Playwright or `webbrowser` module for controlling browser.

#### [NEW] [system.py](file:///e:/LUMI%20AI/lumi/tools/system.py)
- OS interaction (volume, brightness, process management).

### UI
#### [NEW] [desktop_ui.py](file:///e:/LUMI%20AI/lumi/ui/desktop_ui.py)
- Modern window with status (Sleeping, Listening, Processing).

#### [NEW] [main.py](file:///e:/LUMI%20AI/lumi/main.py)
- Entry point. Initializes config, UI, and starts the Orchestrator thread.

### Enhancements
#### [NEW] [weather.py](file:///e:/LUMI%20AI/lumi/tools/weather.py)
- Implementation of OpenMeteo API using `openmeteo-requests` and `pandas`.

#### [MODIFY] [tts.py](file:///e:/LUMI%20AI/lumi/voice/tts.py)
- Add ElevenLabs support if API key is present.

#### [NEW] [splash.py](file:///e:/LUMI%20AI/lumi/ui/splash.py)
- Cinematic launch screen with animations.

#### [MODIFY] [desktop_ui.py](file:///e:/LUMI%20AI/lumi/ui/desktop_ui.py)
- Styling improvements (gradients, icons) for a "gorgeous" look.

#### [NEW] [README.md](file:///e:/LUMI%20AI/README.md)
- Documentation for GitHub.

## Verification Plan


### Automated Tests
- Unit tests for the Router logic (mocking inputs).
- Unit tests for Memory storage/retrieval.

### Manual Verification
- **Wake Word**: Speak "Lumi" and verify it wakes up.
- **Routing**: Ask a coding question and verify GPT is called. Ask a general question and verify Gemini is called.
- **Tools**: Ask to open a pending website and verify it opens.
- **UI**: Observe state changes (Idle -> Listening -> Responding).
