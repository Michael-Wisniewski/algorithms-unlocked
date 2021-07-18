def put_together_LCS(X, Y, l, i, j):
    """Time complexity (without LCS) is O(n+m), where n - number of vertices, m - number of edges.

    >>> X = 'CATCGA'
    >>> Y = 'GTACCGTCA'
    >>> l = LCS(X, Y)
    >>> X = ' ' + X
    >>> Y = ' ' + Y
    >>> i = len(X) - 1
    >>> j = len(Y) - 1
    >>> put_together_LCS(X, Y, l, i, j)
    'CTCA'
    """
    if l[i][j] == 0:
        return ''
    else:
        if X[i] == Y[j]:
            return put_together_LCS(X, Y, l, i-1, j-1) + X[i]
        elif l[i][j-1] > l[i-1][j]:
            return put_together_LCS(X, Y, l, i, j-1)
        else:
            return put_together_LCS(X, Y, l, i-1, j)

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
