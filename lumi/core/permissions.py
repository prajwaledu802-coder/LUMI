import logging

logger = logging.getLogger("Permissions")

class Permissions:
    LEVELS = {
        "READ_ONLY": 0,
        "USER": 1,
        "ADMIN": 2
    }
    
    def __init__(self, default_level="USER"):
        self.current_level = self.LEVELS.get(default_level, 1)

    def check(self, required_level_name):
        required_level = self.LEVELS.get(required_level_name, 2)
        if self.current_level >= required_level:
            return True
        else:
            logger.warning(f"Permission denied. Required: {required_level_name}, Current: {self.current_level}")
            return False

    def request_confirmation(self, action_description):
        # In a real UI, this would pop up a dialog
        logger.info(f"Permissions: ACTION REQUIRES CONFIRMATION -> {action_description}")
        # For prototype, we assume implicit consent if level is high enough, or return False to simulate "needs UI"
        # We'll return True for now but log it.
        return True
