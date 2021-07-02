from collections import deque

def topological_sort(G):
    """Time complexity: Θ(n + m). n - number of vertices, m - number of edges.
    Adding and removing first element from next_vertice takes O(1).
    
    0   1  3
    |  /\  |
     \/  \ |
      2    4
       \  /
        \/
         5
         |
         |
         6

    >>> dag = {
    ... 0: [2],
    ... 1: [2, 4],
    ... 2: [5],
    ... 3: [4],
    ... 4: [5],
    ... 5: [6],
    ... 6: [],
    ... }
    >>> topological_sort(dag)
    [0, 1, 2, 3, 4, 5, 6]
    """
    n = len(G)
    entry_degrees = [0] * n
    sorted_vertices = []

    for u, edges in G.items():
        for v in edges:
            entry_degrees[v] += 1

    next_vertice = deque([])
    for u, entry_degree in enumerate(entry_degrees):
        if entry_degree == 0:
            next_vertice.append(u)

    # this loop can be replaced by for _ in range(0,n)
    while next_vertice:
        u = next_vertice.popleft()
        sorted_vertices.append(u)

        for v in G[u]:
            entry_degrees[v] -= 1

            if entry_degrees[v] == 0:
                next_vertice.appendleft(v)

    return sorted_vertices
