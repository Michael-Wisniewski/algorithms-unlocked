from collections import deque

def shortest_path(G, s):
    """

    >>> dag = {
    ... 0: [{'v': 1, 'w': 5}, {'v': 2, 'w': 3}],
    ... 1: [{'v': 2, 'w': 2}, {'v': 3, 'w': 6}],
    ... 2: [{'v': 3, 'w': 7}, {'v': 4, 'w': 4}, {'v': 5, 'w': 2}],
    ... 3: [{'v': 4, 'w': -1}, {'v': 5, 'w': 1}],
    ... 4: [{'v': 5, 'w': -2}],
    ... 5: []
    ... }
    >>> shortest_path(dag)

  
    """
    infinity = 100000

    shortest = []
    previus = []


    sorted_vertives = topological_sort(G)


def topological_sort(G):
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



dag = {
0: [{'v': 1, 'w': 5}, {'v': 2, 'w': 3}],
1: [{'v': 2, 'w': 2}, {'v': 3, 'w': 6}],
2: [{'v': 3, 'w': 7}, {'v': 4, 'w': 4}, {'v': 5, 'w': 2}],
3: [{'v': 4, 'w': -1}, {'v': 5, 'w': 1}],
4: [{'v': 5, 'w': -2}],
5: []
}

print(topological_sort(dag))
