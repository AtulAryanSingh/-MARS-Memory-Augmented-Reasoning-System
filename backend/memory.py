from datetime import datetime

# In-memory store (user -> list of memories)
MEMORY_DB = {}


def get_user_memory(user: str):
    return MEMORY_DB.setdefault(user, [])


# -------------------------
# CREATE MEMORY
# -------------------------
def add_memory(user: str, text: str, importance: float):
    memory = {
        "text": text,
        "importance": importance,
        "timestamp": datetime.utcnow().isoformat(),
        "active": True
    }
    get_user_memory(user).append(memory)
    return memory


# -------------------------
# READ MEMORY
# -------------------------
def read_memory(user: str):
    return [m for m in get_user_memory(user) if m["active"]]


# -------------------------
# DELETE MEMORY
# -------------------------
def delete_memory(user: str, text: str):
    for m in get_user_memory(user):
        if m["text"] == text and m["active"]:
            m["active"] = False
    return {"status": "deleted"}


# -------------------------
# UPDATE / CONFLICT HANDLING
# -------------------------
def update_memory(user: str, new_text: str):
    """
    Handles:
    - 'I like birds'
    - 'I don't like birds'
    """

    memories = get_user_memory(user)

    # simple rule-based detection
    if "don't like" in new_text.lower():
        target = new_text.lower().replace("don't like", "").strip()

        # deactivate old preference
        for m in memories:
            if target in m["text"].lower():
                m["active"] = False

        # store new negative memory
        return add_memory(user, new_text, 0.9)

    else:
        # normal add
        return add_memory(user, new_text, 0.8)
