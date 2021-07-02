from collections import deque

def shortest_path(G, s):
    """Time complexity: Θ(n + m). n - number of vertices, m - number of edges.

    >>> dag = {
    ... 0: [{'v': 1, 'w': 5}, {'v': 2, 'w': 3}],
    ... 1: [{'v': 2, 'w': 2}, {'v': 3, 'w': 6}],
    ... 2: [{'v': 3, 'w': 7}, {'v': 4, 'w': 4}, {'v': 5, 'w': 2}],
    ... 3: [{'v': 4, 'w': -1}, {'v': 5, 'w': 1}],
    ... 4: [{'v': 5, 'w': -2}],
    ... 5: []
    ... }
    >>> shortest_path(dag, 1)
    ([100000, 0, 2, 6, 5, 3], [None, None, 1, 1, 3, 4])
    """
    infinity = 100000
    n = len(G)

    shortest = [infinity] * n
    shortest[s] = 0
    previous = [None] * n

    sorted_vertives = topological_sort(G)

    for u in sorted_vertives:
        for edge in G[u]:
            relax(u, edge['v'], edge['w'],  shortest, previous)

    return shortest, previous

def relax(u, v, weight, shortest, previous):
    """Time complexity O(1).
    
    >>> shortest = [0, 1000]
    >>> previous = [None, None]
    >>> relax(0, 1, 2, shortest, previous)
    >>> shortest
    [0, 2]
    >>> previous
    [None, 0]
    """
    if shortest[u] + weight < shortest[v]:
        shortest[v] = shortest[u] + weight
        previous[v] = u

def topological_sort(G):
    """Time complexity: Θ(n + m). n - number of vertices, m - number of edges.
    Adding and removing first element from next_vertice takes O(1).

    >>> dag = {
    ... 2: [{'v': 3, 'w': 7}, {'v': 4, 'w': 4}, {'v': 5, 'w': 2}],
    ... 1: [{'v': 2, 'w': 2}, {'v': 3, 'w': 6}],
    ... 4: [{'v': 5, 'w': -2}],
    ... 3: [{'v': 4, 'w': -1}, {'v': 5, 'w': 1}],
    ... 5: [],
    ... 0: [{'v': 1, 'w': 5}, {'v': 2, 'w': 3}]
    ... }
    >>> topological_sort(dag)
    [0, 1, 2, 3, 4, 5]
    """
    n = len(G)
    entry_degrees = [0] * n
    sorted_vertices = []

    for u, edges in G.items():
        for edge in edges:
            entry_degrees[edge['v']] += 1

    next_vertice = deque([])
    for u, entry_degree in enumerate(entry_degrees):
        if entry_degree == 0:
            next_vertice.append(u)

    while next_vertice:
        u = next_vertice.popleft()
        sorted_vertices.append(u)

        for edge in G[u]:
            entry_degrees[edge['v']] -= 1

            if entry_degrees[edge['v']] == 0:
                next_vertice.appendleft(edge['v'])

    return sorted_vertices
