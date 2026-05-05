from dataclasses import dataclass, field
import time

@dataclass
class MemoryItem:
    text: str
    importance: float
    user: str
    timestamp: float = field(default_factory=time.time)