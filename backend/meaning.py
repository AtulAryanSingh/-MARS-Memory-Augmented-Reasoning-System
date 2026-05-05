def compute_importance(text: str) -> float:
    text = text.lower()

    if "i like" in text:
        return 0.9
    if "i want" in text:
        return 0.8
    if "important" in text:
        return 0.85

    return 0.4


def extract_relations(user: str, text: str):
    text = text.lower()
    relations = []

    # FIXED: always anchor user correctly
    if "i like" in text:
        obj = text.replace("i like", "").strip()

        relations.append((f"user:{user}", "likes"))
        relations.append(("likes", obj))

    if "birds" in text:
        relations.append(("birds", "nature"))

    if "fly" in text:
        relations.append(("birds", "fly"))

    if "sky" in text:
        relations.append(("birds", "sky"))

    return relations