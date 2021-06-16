def devide(A, p, r):
    """If the partition sizes are not balanced, you can add a random selection A[r]
       or chose the mean element from three randomly selected.
       Just swap the selected element with the last one in the list. 
    """
    q = p
    
    for u in range(p, r):
        if A[u] <= A[r]:
            temp = A[q]
            A[q] = A[u]
            A[u] = temp
            q += 1

    temp = A[q]
    A[q] = A[r]
    A[r] = temp
    return q

def sort(A, p, r):
    """Time complexity: max Θ(n**2), min Θ(nlgn), average Θ(nlgn). 
       Memory consumption: O(n).
       Replacements max: Θ(n**2).

    >>> numbers =  [8, 6, 7, 4, 5, 2, 3, 1]
    >>> numbers_count = 8
    >>> p = 0
    >>> r = numbers_count - 1
    >>> sort(numbers, p, r)
    [1, 2, 3, 4, 5, 6, 7, 8]
    """

    if p >=r:
        pass
    else:
        q = devide(A, p, r)
        sort(A, p, q - 1)
        sort(A, q + 1, r)

    return A
