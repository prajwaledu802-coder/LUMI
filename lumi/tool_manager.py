import logging
from lumi.tools.browser import BrowserTool
from lumi.tools.system import SystemTool
from lumi.tools.files import FileTool
from lumi.tools.music import MusicTool

logger = logging.getLogger("ToolManager")

class ToolManager:
    def __init__(self):
        self.browser = BrowserTool()
        self.system = SystemTool()
        self.files = FileTool()
        self.music = MusicTool()

    def handle_tool_request(self, tool_name, action, **kwargs):
        """Generic handler for AI to call tools."""
        logger.info(f"Tool Request: {tool_name}.{action} ({kwargs})")
        
        # This is a simple dispatcher. 
        # In a real agentic flow, the LLM would output JSON calling specific functions.
        # For now, we map manually or assume the LLM output is processed elsewhere.
        
        if tool_name == "browser":
            if action == "open":
                self.browser.open_url(kwargs.get("url"))
            elif action == "search":
                self.browser.search_google(kwargs.get("query"))
                
        elif tool_name == "music":
            if action == "play":
                self.music.play_music(kwargs.get("song"))
                
        # ... logic continues
