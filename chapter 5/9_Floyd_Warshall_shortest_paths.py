def shortest_path(G):
    """ ddd Θ (n**3) for finding all shartest paths.
    Works for negative weights but not for cyclic graph.
    memory n2 - if we do not store history of moves
    elsewhere n^3


    >>> dg = {
    ... 0: [{'v': 1, 'w': 3}, {'v': 2, 'w': 8}],
    ... 1: [{'v': 3, 'w': 1}],
    ... 2: [{'v': 1, 'w': 4}],
    ... 3: [{'v': 0, 'w': 2}, {'v': 2, 'w': -5}],
    ... }
    >>> shortest_path(dg)
    ([0, 5, 8, 4, 7], [None, 3, 1, 0, 3])
    """
    n = len(G)
    infinity = 100000

    shortest = []
    previous = []

    for _ in range(n):
        temp_list_1 = []
        temp_list_2 = []
        for _ in range(n + 1):
            temp_list_1.append([infinity] * n)
            temp_list_2.append([None] * n)
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

    
                    

    # for i in range(n):
    #     for j in range(n):
    #         print(shortest[i][j][0], end=' ')
    #     print()

    # for i in range(n):
    #     for j in range(n):
    #         print(previous[i][j][0], end=' ')
    #     print()

