def modular_exponentiation(x, d, n):
    """Time complexity for small numbers: Θ(lg d)- where x, d, n are integers.
    x and d are non negative, n is positive
    Result: (x^d)mod n

    >>> x = 2
    >>> d = 3
    >>> n = 6
    >>> modular_exponentiation(x, d, n)
    2
    """
    if d == 0:
        return 1

    if d % 2 == 0:
        z = modular_exponentiation(x, d / 2, n)
        return z**2 % n
    else:
        z = modular_exponentiation(x, (d - 1) / 2, n)
        return (x**2 * x) % n
