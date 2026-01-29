import webbrowser
import logging

logger = logging.getLogger("BrowserTool")

class BrowserTool:
    @staticmethod
    def open_url(url):
        logger.info(f"Opening URL: {url}")
        if not url.startswith("http"):
            url = "https://" + url
        webbrowser.open(url)

    @staticmethod
    def search_google(query):
        logger.info(f"Searching Google for: {query}")
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)

    @staticmethod
    def open_browser():
        logger.info("Opening default browser")
        webbrowser.open("https://google.com")
