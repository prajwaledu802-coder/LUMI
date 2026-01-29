import json
import os
import logging

logger = logging.getLogger("Memory")

class Memory:
    def __init__(self, memory_file="data/memory.json"):
        self.memory_file = memory_file
        self.data = self._load_memory()

    def _load_memory(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Failed to load memory: {e}")
                return {}
        return {}

    def save_memory(self):
        try:
            os.makedirs(os.path.dirname(self.memory_file), exist_ok=True)
            with open(self.memory_file, 'w') as f:
                json.dump(self.data, f, indent=4)
        except Exception as e:
            logger.error(f"Failed to save memory: {e}")

    def set(self, key, value):
        self.data[key] = value
        self.save_memory()

    def get(self, key, default=None):
        return self.data.get(key, default)
