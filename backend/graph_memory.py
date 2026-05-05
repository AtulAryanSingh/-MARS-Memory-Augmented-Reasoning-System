graph_memory = {}

def add_relation(a: str, b: str):
    if a not in graph_memory:
        graph_memory[a] = []

    if b not in graph_memory[a]:
        graph_memory[a].append(b)


def get_graph():
    return graph_memory