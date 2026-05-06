from collections import defaultdict
from time import time
from models import MemoryItem

memory_store = defaultdict(list)


def reset_memory(user: str):
    memory_store[user] = []


def update_memory(user: str, item: MemoryItem):

    if not hasattr(item, "timestamp") or item.timestamp is None:
        item.timestamp = time()

    memory_store[user].append(item)
    return item


def get_memory(user: str):
    return memory_store[user]


def get_active_memory(user: str):
    return memory_store[user]
