def sort(numbers, numbers_count):
    """Time complexity: max Θ(n**2), min Θ(n), average Θ(n**2). 
       Memory consumption: O(n).
       Replacements max: Θ(n**2), min Θ(1).

    >>> numbers =  [8, 6, 7, 4, 5, 2, 3, 1]
    >>> numbers_count = 8
    >>> sort(numbers, numbers_count)
    [1, 2, 3, 4, 5, 6, 7, 8]
    """

    for i in range(1, numbers_count):
        temp = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > temp:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = temp

    return numbers
