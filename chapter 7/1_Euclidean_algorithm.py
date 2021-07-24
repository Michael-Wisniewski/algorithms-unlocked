from math import floor

def greatest_common_divisor(a, b):
    """Time complexity: O(lg b), where a and are integers.
    Result: g, i, j where g is the greatest common divisor for i and j where g = a * i + b * j 

    >>> a = 10
    >>> b = 0
    >>> greatest_common_divisor(a, b)
    (10, 1, 0)
    >>> a = 30
    >>> b = 18
    >>> greatest_common_divisor(a, b)
    (6, -1, 2)
    """
    if b == 0:
        return a, 1, 0
    
    g, i_prim, j_prim = greatest_common_divisor(b, a % b)
    i = j_prim
    j = i_prim - floor(a / b) * j_prim
    return g, i ,j
