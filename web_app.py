import streamlit as st
import sys
import os
from dotenv import load_dotenv

# Ensure we can import from root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Load Env
load_dotenv(dotenv_path="e:\\LUMI AI\\JARVIS-AI-Assistant-main\\.env")

from lumi.ai.router import AIRouter
from lumi.tools.weather import WeatherTool
from lumi.tools.browser import BrowserTool

# Initialize logic
router = AIRouter()
weather = WeatherTool()

st.set_page_config(page_title="LUMI AI", page_icon="🔵", layout="wide")

# Custom CSS for Dark Mode/Glassmorphism feel
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #00A8FF;
    }
    .stTextInput > div > div > input {
        background-color: #262730;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.title("🔵 LUMI AI Web Interface")
st.text("Professional Hybrid AI Assistant")

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input
if prompt := st.chat_input("Ask LUMI..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Process
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Check for tools first (Simple check)
        if "weather" in prompt.lower():
            response = weather.get_weather() # Simple mock or real
            full_response = f"**Weather Report:**\n{response}"
        elif "open google" in prompt.lower():
            BrowserTool.open_browser()
            full_response = "Opening Google in server browser..."
        else:
            # AI
            full_response = router.route_and_generate(prompt)
            
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
