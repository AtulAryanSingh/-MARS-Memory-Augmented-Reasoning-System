from collections import defaultdict

graph = defaultdict(list)


def add_relation(a, b):
    if b not in graph[a]:
        graph[a].append(b)


def get_graph():
    return dict(graph)