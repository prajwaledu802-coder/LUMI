import webbrowser
import logging

logger = logging.getLogger("MusicTool")

class MusicTool:
    @staticmethod
    def play_music(query=None):
        if query:
            logger.info(f"Playing music: {query}")
            # Use YouTube Music or Spotify Web
            url = f"https://music.youtube.com/search?q={query}"
            webbrowser.open(url)
        else:
            logger.info("Opening Music Player")
            webbrowser.open("https://music.youtube.com")
