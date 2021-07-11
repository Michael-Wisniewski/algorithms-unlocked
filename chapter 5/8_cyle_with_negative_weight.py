from collections import deque

def find_cycle_with_negative_weight(G, shortest, previous):
    """Time complexity O(n + m), where n - number of vertices, m - number of edges.
    
    >>> dg = {
    ... 0: [{'v': 1, 'w': 6}, {'v': 3, 'w': 7}],
    ... 1: [{'v': 3, 'w': 4}, {'v': 2, 'w': 5}, {'v': 4, 'w': -4}],
    ... 2: [{'v': 1, 'w': -2}],
    ... 3: [{'v': 2, 'w': -3}, {'v': 4, 'w': 9}],
    ... 4: [{'v': 0, 'w': 2}, {'v': 2, 'w': 7}]
    ... }
    >>> s = 0
    >>> shortest, previous = shortest_path(dg, s)
    >>> find_cycle_with_negative_weight(dg, shortest, previous)
    deque([3, 2, 1])
    """
    n = len(G)
    v = None

    for u in G.keys():
        for edge in G[u]:
            if shortest[u] + edge['w'] < shortest[edge['v']]:
                v = edge['v']

    if v is None:
        return []

    visited = [False] * n
    x = v

    while visited[x] is False:
        visited[x] = True
        x = previous[x]

    v = previous[x]
    vertices_cycle = deque([x])

    while v != x:
        vertices_cycle.appendleft(v)
        v = previous[v]

    return vertices_cycle

def shortest_path(G, s):
    """Time complexity O(n*m), where n - number of vertices, m - number of edges.
    
    >>> dag = {
    ... 0: [{'v': 1, 'w': 6}, {'v': 3, 'w': 7}],
    ... 1: [{'v': 3, 'w': 8}, {'v': 2, 'w': 5}, {'v': 4, 'w': -4}],
    ... 2: [{'v': 1, 'w': -2}],
    ... 3: [{'v': 2, 'w': -3}, {'v': 4, 'w': 9}],
    ... 4: [{'v': 0, 'w': 2}, {'v': 2, 'w': 7}]
    ... }
    >>> s = 0
    >>> shortest_path(dag, s)
    ([0, 2, 4, 7, -2], [None, 2, 3, 0, 1])
    """ 
    infinity = 100000
    n = len(G)

    shortest = [infinity] * n
    shortest[s] = 0
    previous = [None] * n

    for _ in range(n-1):
        for u, edges in G.items():
            for edge in edges:
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
