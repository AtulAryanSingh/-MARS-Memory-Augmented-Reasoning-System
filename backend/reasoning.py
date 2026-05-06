from memory import get_active_memory


def answer_query(query: str, user: str = "test_user"):

    query = (query or "").lower().strip()
    memories = get_active_memory(user)

    if not memories:
        return "no preference"

    # --------------------------------------
    # STEP 1: BUILD FINAL STATE TABLE
    # --------------------------------------
    state = {}

    for m in sorted(memories, key=lambda x: x.timestamp):

        text = m.text.lower()

        # NEGATION = DISLIKE (ALWAYS OVERWRITE)
        if "dont like" in text or "don't like" in text:
            entity = text.replace("i dont like", "").replace("i don't like", "").strip()
            state[entity] = "dislike"

        # LIKE
        elif "like" in text:
            entity = text.replace("i like", "").strip()

            # ONLY set if not already overridden
            if state.get(entity) != "dislike":
                state[entity] = "like"

    # --------------------------------------
    # STEP 2: QUERY
    # --------------------------------------
    if "like" not in query:
        return "unknown query"

    liked = [k for k, v in state.items() if v == "like"]
    disliked = [k for k, v in state.items() if v == "dislike"]

    if liked:
        return f"i like {liked[0]}"

    if disliked:
        return f"i dont like {disliked[0]}"

    return "no preference"