def return_shortest_path(G, start_vertice, end_vertice):
    """Time complexity without finding shortest path: Θ(n), where n - number of vertices.
    Memory consumption: Θ(n).

    >>> dg = {
    ... 0: [{'v': 1, 'w': 3}, {'v': 2, 'w': 8}],
    ... 1: [{'v': 3, 'w': 1}],
    ... 2: [{'v': 1, 'w': 4}],
    ... 3: [{'v': 0, 'w': 2}, {'v': 2, 'w': -5}],
    ... }
    >>> start_vertice = 0
    >>> end_vertice = 2
    >>> return_shortest_path(dg, start_vertice, end_vertice)
    (-1, [0, 1, 3, 2])
    """
    shortest, previous = shortest_path(G)
    length = shortest[start_vertice][end_vertice][-1]
    path = []

    previous_vertice = end_vertice
    path.append(previous_vertice)

    for previous_index in range(len(G), 1, -1):
        previous_vertice = previous[start_vertice][previous_vertice][previous_index]

        if previous_vertice != path[-1]:
            path.append(previous_vertice)

    path.reverse()

    return length, path

def shortest_path(G):
    """Time complexity: Θ(n^3) for finding all shartest paths.
    Works for negative weights but not for cyclic graphs.

    Memory consumption: Θ(n^3).
    It will be Θ(n^2), if we do not store history of moves.

    >>> dg = {
    ... 0: [{'v': 1, 'w': 3}, {'v': 2, 'w': 8}],
    ... 1: [{'v': 3, 'w': 1}],
    ... 2: [{'v': 1, 'w': 4}],
    ... 3: [{'v': 0, 'w': 2}, {'v': 2, 'w': -5}],
    ... }
    >>> shortest_path(dg)
    ([[[0, 0, 0, 0, 0], [3, 3, 3, 3, 3], [8, 8, 8, 8, -1], [100000, 100000, 4, 4, 4]], [[100000, 100000, 100000, 100000, 3], [0, 0, 0, 0, 0], [100000, 100000, 100000, 100000, -4], [1, 1, 1, 1, 1]], [[100000, 100000, 100000, 100000, 7], [4, 4, 4, 4, 4], [0, 0, 0, 0, 0], [100000, 100000, 5, 5, 5]], [[2, 2, 2, 2, 2], [100000, 5, 5, -1, -1], [-5, -5, -5, -5, -5], [0, 0, 0, 0, 0]]], [[[None, None, None, None, None], [0, 0, 0, 0, 0], [0, 0, 0, 0, 3], [None, None, 1, 1, 1]], [[None, None, None, None, 3], [None, None, None, None, None], [None, None, None, None, 3], [1, 1, 1, 1, 1]], [[None, None, None, None, 3], [2, 2, 2, 2, 2], [None, None, None, None, None], [None, None, 1, 1, 1]], [[3, 3, 3, 3, 3], [None, 0, 0, 2, 2], [3, 3, 3, 3, 3], [None, None, None, None, None]]])
    """
    n = len(G)
    infinity = 100000

    shortest = []
    previous = []

    # We can not use [val] * n because all cells will use same memory reference.
    for _ in range(n):
        temp_list_1 = []
        temp_list_2 = []
        for _ in range(n):
            temp_list_1.append([infinity] * (n + 1))
            temp_list_2.append([None] * (n + 1))
        shortest.append(temp_list_1)
        previous.append(temp_list_2)

    for u in range(n):
        shortest[u][u][0] = 0

    for u in range(n):
        for v in range(n):
            for edge in G[u]:
                if edge['v'] == v:
                    shortest[u][v][0] = edge['w']
                    previous[u][v][0] = u

    for x in range(n):
        for u in range(n):
            for v in range(n):
                if shortest[u][v][x] > shortest[u][x][x] + shortest[x][v][x]:
                    shortest[u][v][x+1] = shortest[u][x][x] + shortest[x][v][x]
                    previous[u][v][x+1] = previous[x][v][x]
                else:
                    shortest[u][v][x+1] = shortest[u][v][x]
                    previous[u][v][x+1] = previous[u][v][x]

    return shortest, previous
