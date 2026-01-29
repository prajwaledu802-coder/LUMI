"""
LUMI AI Backend API
Connects web interface to Gemini AI for intelligent responses
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
from dotenv import load_dotenv

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()

from lumi.ai.router import AIRouter
from lumi.tools.weather import WeatherTool
from lumi.tools.browser import BrowserTool
from lumi.tools.music import MusicTool

app = Flask(__name__)
CORS(app)  # Allow requests from HTML frontend

# Initialize AI and tools
ai_router = AIRouter()
weather_tool = WeatherTool()
music_tool = MusicTool()

# LUMI's personality system prompt
LUMI_SYSTEM_PROMPT = """You are LUMI, a calm, intelligent, and caring AI assistant. 

PERSONALITY:
- Speak like a friendly teen girl - casual, warm, and natural
- Be brief and direct (1-2 sentences max)
- Never use excessive emojis or hearts
- Sound human, not robotic

CAPABILITIES:
- Play music on YouTube
- Open websites (YouTube, Instagram, Google, etc.)
- Activate camera for object detection
- Answer questions
- Help with tasks

RESPONSE RULES:
1. If user asks to play music → respond: "Opening YouTube for that now."
2. If user asks to open a website → respond: "Sure, opening [website]."
3. If user asks about camera → respond: "Activating camera."
4. For greetings → respond naturally: "Hey! What can I help with?"
5. For questions → answer directly and briefly

NEVER:
- Repeat the same greeting multiple times
- Ask "how are you?" unless user asks first
- Use multiple hearts or emojis
- Give long explanations

Be smart, helpful, and natural."""

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests from frontend"""
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Detect command type
        message_lower = user_message.lower()
        action = None
        
        # Music commands
        if any(word in message_lower for word in ['play', 'music', 'song']):
            action = {
                'type': 'music',
                'query': user_message
            }
            response_text = "Opening YouTube for that now."
        
        # Browser commands
        elif 'open' in message_lower or any(site in message_lower for site in ['youtube', 'instagram', 'google', 'github']):
            if 'youtube' in message_lower:
                action = {'type': 'browser', 'url': 'https://youtube.com'}
                response_text = "Sure, opening YouTube."
            elif 'instagram' in message_lower:
                action = {'type': 'browser', 'url': 'https://instagram.com'}
                response_text = "Sure, opening Instagram."
            elif 'google' in message_lower:
                action = {'type': 'browser', 'url': 'https://google.com'}
                response_text = "Sure, opening Google."
            else:
                action = {'type': 'browser', 'url': f'https://google.com/search?q={user_message}'}
                response_text = "Searching for that."
        
        # Camera commands
        elif any(word in message_lower for word in ['camera', 'vision', 'scan', 'see', 'what is this']):
            action = {'type': 'camera'}
            response_text = "Activating camera now."
        
        # Weather commands
        elif 'weather' in message_lower:
            weather_data = weather_tool.get_weather()
            response_text = f"Weather: {weather_data}"
            action = None
        
        # General conversation - use AI
        else:
            # Create context-aware prompt
            full_prompt = f"{LUMI_SYSTEM_PROMPT}\n\nUser: {user_message}\nLUMI:"
            response_text = ai_router.route_and_generate(full_prompt)
            
            # Clean up response (remove any system prompt leakage)
            if "LUMI:" in response_text:
                response_text = response_text.split("LUMI:")[-1].strip()
            
            action = None
        
        return jsonify({
            'response': response_text,
            'action': action
        })
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            'response': "I'm having a little trouble right now. Can you try again?",
            'action': None
        }), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'service': 'LUMI AI Backend'})

if __name__ == '__main__':
    print("🔵 LUMI AI Backend starting...")
    print("📡 API will be available at: http://localhost:5000")
    print("🔑 Make sure GEMINI_API_KEY is set in your .env file")
    app.run(host='0.0.0.0', port=5000, debug=True)
