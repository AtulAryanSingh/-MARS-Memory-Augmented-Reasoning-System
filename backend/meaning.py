# meaning.py

import re


def compute_importance(text: str) -> float:
    text = text.lower()

    if "like" in text:
        return 0.8
    if "dont like" in text or "don't like" in text:
        return 0.8

    return 0.4


def extract_entity(text: str):
    text = text.lower()
    cleaned = re.sub(r"(i|like|dont|don't)", "", text)
    words = cleaned.split()
    return words[-1] if words else "unknown"


def canonicalize(text: str):
    text = text.lower().strip()

    if "don't like" in text or "dont like" in text:
        return {
            "type": "dislike",
            "entity": extract_entity(text)
        }

    if "like" in text:
        return {
            "type": "like",
            "entity": extract_entity(text)
        }

    return {
        "type": "unknown",
        "entity": text
    }


def extract_relations(user: str, text: str):
    parsed = canonicalize(text)
    relations = []

    if parsed["type"] == "like":
        relations.append((f"user:{user}", "likes"))
        relations.append(("likes", parsed["entity"]))

    elif parsed["type"] == "dislike":
        relations.append((f"user:{user}", "dislikes"))
        relations.append(("dislikes", parsed["entity"]))

    return relations