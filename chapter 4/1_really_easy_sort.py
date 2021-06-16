def sort(A, n):
    """Time complexity: Θ(n), memory consumption - O(n).
    
    >>> numbers = [1, 2, 2, 1, 2, 1, 1]
    >>> numbers_count = 7
    >>> sort(numbers, numbers_count)
    [1, 1, 1, 1, 2, 2, 2]
    """

    k = 0

    for i in range(0, n):
        if A[i] == 1:
            k += 1
    
    for i in range(0, k):
        A[i] = 1

    for i in range(k, n):
        A[i] = 2

    return A
