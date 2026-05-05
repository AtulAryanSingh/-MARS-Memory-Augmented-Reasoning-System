from llm_layer import llm_generate


def build_answer(query: str, paths: list):
    query = query.lower()

    # convert paths → structured context
    context_lines = []
    for a, b in paths:
        context_lines.append(f"{a} → {b}")

    context = "\n".join(context_lines)

    # fallback logic (no LLM)
    if "user like" in query:
        likes = [b for a, b in paths if a == "likes"]

        base_answer = (
            f"User likes {', '.join(likes)}."
            if likes else
            "User preference unknown."
        )
    else:
        base_answer = "I don't have enough information."

    # 🔥 HYBRID STEP (LLM AUGMENTATION)
    enhanced = llm_generate(query, context)

    return {
        "base_answer": base_answer,
        "llm_answer": enhanced,
        "context_used": context
    }