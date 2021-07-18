def LCS(X, Y):
    """Time complexity: Θ(m*n), where m and n are lengths of words.

    >>> X = 'CATCGA'
    >>> Y = 'GTACCGTCA'
    >>> LCS(X, Y)
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1, 1, 2], [0, 0, 1, 1, 1, 1, 1, 2, 2, 2], [0, 0, 1, 1, 2, 2, 2, 2, 3, 3], [0, 1, 1, 1, 2, 2, 3, 3, 3, 3], [0, 1, 1, 2, 2, 2, 3, 3, 3, 4]]
    """
    X = ' ' + X
    Y = ' ' + Y

    m = len(X)
    n = len(Y)
    l = []

    for _ in range(m):
        l.append([0] * n)
    
    for i in range(1, m):
        for j in range(1, n):
            if X[i] == Y[j]:
                l[i][j] = l[i-1][j-1] + 1
            else:
                l[i][j] = max(l[i][j-1], l[i-1][j])

    return l
