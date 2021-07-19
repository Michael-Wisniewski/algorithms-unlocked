def search_pattern(X, Y):
    """Time complexity: O(m+n), where m is length of pattern and n length of string.

    >>> X = 'ABABAABA'
    >>> Y = 'ABCABAB ABABABAABAC ABABAABA'
    >>> search_pattern(X, Y)
    [10, 20]
    """
    m = len(X)
    n = len(Y)
    i = j = 0
    lookup_list = finite_automaton(X)
    patterns_found = []

    while i < n:
        if Y[i] == X[j]:
            if j == (m - 1):
                patterns_found.append(i - j)
                j = 0
            else:
                j += 1
            i += 1
        elif j > 0:
            j = lookup_list[j - 1]
        else:
            i += 1

    return patterns_found

def finite_automaton(X):
    """
    >>> X = 'ABABAABA'
    >>> finite_automaton(X)
    [0, 0, 1, 2, 3, 1, 2, 3]
    """
    m = len(X)
    lookup_list = [0] * m
    i = 0
    j = 1

    while j < m:
        if X[i] == X[j]:
            if i == 0 :
                lookup_list[j] = 1
            else:
                lookup_list[j] = lookup_list[j - 1] + 1
            i += 1
            j += 1
        elif i > 0:    
            i = lookup_list[i - 1]
        else:
            j += 1

    return lookup_list
