def put_together_transform_table(operation, i, j):
    """Time complexity (without LCS) is O(n+m), where n - number of vertices, m - number of edges.

    >>> X = 'ACAAGC'
    >>> Y = 'CCGT'
    >>> CC = -1
    >>> CR = 1
    >>> CD = CI = 2
    >>> cost, operation = compute_transform_tables(X, Y, CC, CR, CD, CI)
    >>> i = 6
    >>> j = 4
    >>> put_together_transform_table(operation, i, j)
    'DCDRCR'
    """
    if i == 0 and j == 0:
        return ''
    elif operation[i][j] == 'C' or operation[i][j] == 'R':
        return put_together_transform_table(operation, i-1, j-1) + operation[i][j]
    elif operation[i][j] == 'D':
        return put_together_transform_table(operation, i-1, j) + operation[i][j]
    else:
        return put_together_transform_table(operation, i, j-1) + operation[i][j]

def compute_transform_tables(X, Y, CC, CR, CD, CI):
    """Time complexity: Θ(m*n), where m and n are lengths of words.

    >>> X = 'ACAAGC'
    >>> Y = 'CCGT'
    >>> CC = -1
    >>> CR = 1
    >>> CD = CI = 2
    >>> compute_transform_tables(X, Y, CC, CR, CD, CI)
    ([[0, 2, 4, 6, 8], [2, 1, 3, 5, 7], [4, 1, 0, 2, 4], [6, 3, 2, 1, 3], [8, 5, 4, 3, 2], [10, 7, 6, 3, 4], [12, 9, 6, 5, 4]], [[None, 'I', 'I', 'I', 'I'], ['D', 'R', 'R', 'R', 'R'], ['D', 'C', 'C', 'I', 'I'], ['D', 'D', 'R', 'R', 'R'], ['D', 'D', 'R', 'R', 'R'], ['D', 'D', 'R', 'C', 'R'], ['D', 'C', 'C', 'D', 'R']])
    """
    X = ' ' + X
    Y = ' ' + Y

    m = len(X)
    n = len(Y)

    cost = []
    operation = []

    for _ in range(m):
        cost.append([None] * n)
        operation.append([None] * n)

    cost[0][0] = 0

    for i in range(1, m):
        cost[i][0] = i * CD
        operation[i][0] = 'D'
    
    for j in range(1, n):
        cost[0][j] = j * CI
        operation[0][j] = 'I'

    for i in range(1, m):
        for j in range(1, n):
            if X[i] == Y[j]:
                cost[i][j] = cost[i-1][j-1] + CC
                operation[i][j] = 'C'
            else:
                cost[i][j] = cost[i-1][j-1] + CR
                operation[i][j] = 'R'

            if cost[i-1][j] + CD < cost[i][j]:
                cost[i][j] = cost[i-1][j] + CD
                operation[i][j] = 'D'

            if cost[i][j-1] + CI < cost[i][j]:
                cost[i][j] = cost[i][j-1] + CI
                operation[i][j] = 'I'

    return cost, operation
