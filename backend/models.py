# models.py

import time


class MemoryItem:
    def __init__(
        self,
        text,
        importance,
        user,
        confidence=0.9,
        source="user_input",
        reason="initial"
    ):
        self.text = text
        self.importance = importance
        self.user = user
        self.timestamp = time.time()
        self.active = True
        self.confidence = confidence
        self.source = source
        self.reason = reason

    def to_dict(self):
        return {
            "text": self.text,
            "importance": self.importance,
            "user": self.user,
            "timestamp": self.timestamp,
            "active": self.active,
            "confidence": self.confidence,
            "source": self.source,
            "reason": self.reason,
        }