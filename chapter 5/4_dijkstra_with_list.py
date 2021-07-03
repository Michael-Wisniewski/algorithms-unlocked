def dijkstra_with_list(G, s):
    """n - number of vertices, m - number of edges
    In total find_min takes Θ(n^2) and relax takes O(m).
    Because m <= n^2, time complexity is O(n^2).

    >>> dag = {
    ... 0: [{'v': 1, 'w': 6}, {'v': 3, 'w': 4}],
    ... 1: [{'v': 3, 'w': 2}, {'v': 2, 'w': 3}],
    ... 2: [{'v': 4, 'w': 4}],
    ... 3: [{'v': 1, 'w': 1}, {'v': 2, 'w': 9}, {'v': 4, 'w': 3}],
    ... 4: [{'v': 0, 'w': 7}, {'v': 2, 'w': 5}]
    ... }
    >>> s = 0
    >>> dijkstra_with_list(dag, s)
    ([0, 5, 8, 4, 7], [None, 3, 1, 0, 3])
    """
    infinity = 100000
    n = len(G)

    shortest = [infinity] * n
    shortest[s] = 0
    previous = [None] * n

    Q = []
    counter = 0

    for v in G.keys():
        Q.append(v)
        counter += 1

    while counter >= 1:
        u = find_min(Q[:counter], shortest)
        temp = Q[u]
        Q[u] = Q[counter - 1]
        Q[counter - 1] = temp
        counter -= 1

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

def find_min(Q, shortest):
    """Time complexity O(n), n - present number of vertices in list Q.

    >>> Q = [4, 1, 2, 3]
    >>> shortest = [0, 6, 100000, 4, 100000]
    >>> find_min(Q, shortest)
    3
    """
    min_v = 0
    min_w = 100000

    for v in Q:
        if shortest[v] <= min_w:
            min_v = v
            min_w = shortest[v]

    return min_v
