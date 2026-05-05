from graph_memory import graph_memory
from response_builder import build_answer


def traverse(start: str, depth: int = 3):
    visited = set()
    paths = []

    def dfs(node, d):
        if d > depth or node in visited:
            return

        visited.add(node)

        for nxt in graph_memory.get(node, []):
            paths.append((node, nxt))
            dfs(nxt, d + 1)

    dfs(start, 0)
    return paths


def detect_intent(query: str):
    query = query.lower()

    if "what does user like" in query or "user like" in query:
        return "preference"

    if "birds" in query:
        return "entity"

    return "unknown"


def answer_query(query: str):

    intent = detect_intent(query)

    if intent == "preference":
        paths = traverse("user:u1")

        # clean preference path only
        filtered = [p for p in paths if "likes" in p or "user:u1" in p]

        return {
            "type": "preference_query",
            "intent": intent,
            "paths": filtered,
            "answer": build_answer(query, filtered)
        }

    if intent == "entity":
        paths = traverse("birds")

        filtered = [p for p in paths if p[0] == "birds"]

        return {
            "type": "entity_query",
            "intent": intent,
            "paths": filtered,
            "answer": build_answer(query, filtered)
        }

    return {
        "type": "unknown",
        "intent": intent,
        "paths": [],
        "answer": "I don't know."
    }