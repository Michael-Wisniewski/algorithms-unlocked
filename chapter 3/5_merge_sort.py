from math import floor


def merge(A, p, q, r):
    B = A[p:q + 1]
    B.append(10000000000)
    C = A[q+1:r + 1]
    C.append(10000000000)
    i, j = 0 , 0

    for k in range(p, r + 1):
        if B[i] <= C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1


def sort(A, p, r):
    """Time complexity: O(nlgn), Ω(nlgn).
       Memory consumption: O(n).
       Inparallel implementation uses a lot of memory to copy an array: O(nlgn + n) = O(nlgn)
       Replacements max: Θ(nlgn).
       Large constant factor compared to select sort and insert sort. 
       In parallel implementation constant factor will be much lower.

    >>> numbers =  [8, 6, 7, 4, 5, 2, 3, 1]
    >>> numbers_count = 8
    >>> p = 0
    >>> r = numbers_count - 1
    >>> sort(numbers, p, r)
    [1, 2, 3, 4, 5, 6, 7, 8]
    """

    if p >= r:
        pass
    else:
        q = floor((p + r) / 2)
        sort(A, p, q)
        sort(A, q + 1, r)
        merge(A, p, q, r)

    return A
