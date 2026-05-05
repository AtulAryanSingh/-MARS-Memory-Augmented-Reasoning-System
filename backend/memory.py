from typing import Dict, List
from models import MemoryItem

memory_store: Dict[str, List[MemoryItem]] = {}

DECAY_RATE = 0.02
REINFORCEMENT_BOOST = 0.08


def get_memory(user: str):
    return memory_store.setdefault(user, [])


def save_memory(user: str, new_item: MemoryItem):
    memory = get_memory(user)

    # 🔁 CHECK IF ALREADY EXISTS (MERGE LOGIC)
    for item in memory:
        if item.text == new_item.text:
            item.importance = min(1.0, item.importance + REINFORCEMENT_BOOST)
            return

    memory.append(new_item)


def apply_decay(user: str):
    memory = get_memory(user)

    for item in memory:
        # ⏳ decay only weak memories
        if item.importance < 0.75:
            item.importance = max(0.0, item.importance - DECAY_RATE)