from memory import get_active_memory


def answer_query(query: str, user: str = "test_user"):

    query = query.lower()

    memories = get_active_memory(user)

    likes = []
    dislikes = []

    # ---------------- BUILD STATE ----------------
    for m in memories:
        text = m.text.lower()

        if "dont like" in text or "don't like" in text:
            entity = text.replace("i dont like", "").replace("i don't like", "").strip()
            dislikes.append(entity)

        elif "i like" in text:
            entity = text.replace("i like", "").strip()
            likes.append(entity)

    # ---------------- QUERY LOGIC ----------------

    # NEGATION TEST HANDLING (critical fix)
    if "don't like" in query or "dont like" in query:
        if dislikes:
            return f"user dislikes {dislikes[0]}"
        return "no preference"

    # DEFAULT PREFERENCE QUERY
    if "like" in query:

        # remove conflicts
        final_likes = [x for x in likes if x not in dislikes]

        if final_likes:
            return f"user likes {final_likes[0]}"

        if dislikes:
            return f"user dislikes {dislikes[0]}"

        return "no preference"

    return "unknown query"