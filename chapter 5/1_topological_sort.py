def sort(G, n):
    """Time complexity: Θ(n + m). N - number of vertices, m - number of edges."""
    entry_degrees = [0] * n
    sorted_vertices = []

    for u, edges in G.items():
        for v in edges:
            entry_degrees[v] += 1

    next_vertice = []
    for u, entry_degree in enumerate(entry_degrees):
        if entry_degree == 0:
            next_vertice.append(u)

    # this loop can be changed by for _ in range(0,n)
    while next_vertice:
        u = next_vertice.pop(0)
        sorted_vertices.append(u)

        for v in dag[u]:
            entry_degrees[v] -= 1

            if entry_degrees[v] == 0:
                next_vertice.insert(0, v)

    return sorted_vertices


#    0  1   3
#    |  |   |
#     \/    |
#      2    4
#       \  /
#        \/
#         5
#         |
#         |
#         6

dag = {
    0: [2],
    1: [2],
    2: [5],
    3: [4],
    4: [5],
    5: [6],
    6: [],
}
vertices_count = 7

sorted_vertices = sort(dag, vertices_count)
print('Sorted vertices:', sorted_vertices)