def factorial(n):
    """Time complexity - O(n), memory consumption - O(n) *
    
    * For small numbers where:
    - multiplication time complexity is O(1)
    - integer variable size is constant

    To check maximum available recursion depth run:
    import sys
    print(sys.getrecursionlimit())

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
