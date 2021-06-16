def wrong_factorial(n):
    """
    Invalid recursive function which will not reach a base case.

    >>> wrong_factorial(1)
    Traceback (most recent call last):
    ...
    RuntimeError: maximum recursion depth exceeded
    """

    if n == 0:
        return 1
    else:
        return wrong_factorial(n + 1) / (n + 1)
