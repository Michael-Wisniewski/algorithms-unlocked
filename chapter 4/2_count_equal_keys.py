def count_equal_keys(A, n, m):
    """Time complexity: Θ(n) if m is constant, memory consumption - Θ(n).

    >>> numbers = [1, 0, 4, 2, 3, 0, 2, 0, 1]
    >>> numbers_count = 9
    >>> max_number = 4
    >>> count_equal_keys(numbers, numbers_count, max_number)
    [3, 2, 2, 1, 1]
    """

    equal_keys = [0] * (m + 1)
    
    for i in range(0, n):
        index = A[i]
        equal_keys[index] += 1

    return equal_keys


def sort_by_counting_equal_keys(A, n, m):
    """Time complexity: Θ(n) if m is constant, memory consumption - Θ(n).
    Works only for natural numbers without metadata.

    >>> numbers = [1, 0, 4, 2, 3, 0, 2, 0, 1]
    >>> numbers_count = 9
    >>> max_number = 4
    >>> sort_by_counting_equal_keys(numbers, numbers_count, max_number)
    [0, 0, 0, 1, 1, 2, 2, 3, 4]
    """

    equal_keys = [0] * (m + 1)
    
    for i in range(0, n):
        index = A[i]
        equal_keys[index] += 1

    sorted_list = []

    for i in range(0, m + 1):
        sorted_list += [i] * equal_keys[i]

    return sorted_list
