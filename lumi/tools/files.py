import os
import subprocess
import logging

logger = logging.getLogger("FileTool")

class FileTool:
    @staticmethod
    def open_file(path):
        logger.info(f"Opening file: {path}")
        if os.path.exists(path):
            os.startfile(path) # Windows only
        else:
            logger.error("File not found.")

    @staticmethod
    def open_folder(path):
        logger.info(f"Opening folder: {path}")
        if os.path.exists(path):
            os.startfile(path)
        else:
            logger.error("Folder not found.")
