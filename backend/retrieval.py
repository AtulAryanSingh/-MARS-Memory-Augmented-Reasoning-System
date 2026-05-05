from config import THRESHOLD

def retrieve(memory_list):
    return [
        m for m in memory_list
        if m.importance >= THRESHOLD
    ]