from math import floor


def dijkstra_with_binary_heap(G, s):
    """Time complexity: O(nlgn), n - number of vertices.

    >>> dag = {
    ... 0: [{'v': 1, 'w': 6}, {'v': 3, 'w': 4}],
    ... 1: [{'v': 3, 'w': 2}, {'v': 2, 'w': 3}],
    ... 2: [{'v': 4, 'w': 4}],
    ... 3: [{'v': 1, 'w': 1}, {'v': 2, 'w': 9}, {'v': 4, 'w': 3}],
    ... 4: [{'v': 0, 'w': 7}, {'v': 2, 'w': 5}]
    ... }
    >>> s = 0
    >>> dijkstra_with_binary_heap(dag, s)
    ([0, 5, 8, 4, 7], [None, 3, 1, 0, 3])
    """
    infinity = 100000
    n = len(G)

    shortest = [infinity] * n
    shortest[s] = 0
    previous = [None] * n

    Q = [v for v in range(n)]
    Q[0] = s
    Q[s] = 0

    for _ in range(n):
        u = Q[0]

        for edge in G[u]:
            relax(u, edge['v'], edge['w'],  shortest, previous)

        Q = pop_min_and_rebuild_heap(Q, shortest)

    return shortest, previous

def pop_min_and_rebuild_heap(Q, shortest):
    """Time complexity: O(nlgn), n - number of verticies.
    Single insertion, deletion (getting minimal value) - O(lgn).

    >>> shortest = [0, 6, 100000, 4, 100000]
    >>> Q = [0, 1, 2, 3, 4]
    >>> pop_min_and_rebuild_heap(Q, shortest)
    [3, 2, 1, 4]
    """
    new_Q = []

    for index, v in enumerate(Q[1:]):
        new_Q.append(v)
        element_index = index
        parent_index = floor((element_index - 1) / 2)

        while (
            element_index != 0 and 
            shortest[new_Q[parent_index]] > shortest[new_Q[element_index]]
        ):
            temp = new_Q[parent_index]
            new_Q[parent_index] = new_Q[element_index]
            new_Q[element_index] = temp

            element_index = parent_index
            parent_index = floor((element_index - 1) / 2)

    return new_Q

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
