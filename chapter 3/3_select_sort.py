def sort(numbers, numbers_count):
    """Time complexity - Θ(n**2), memory consumption - O(n), replacements O(n).

    >>> numbers =  [8, 6, 7, 4, 5, 2, 3, 1]
    >>> numbers_count = 8
    >>> sort(numbers, numbers_count)
    [1, 2, 3, 4, 5, 6, 7, 8]
    """

    for i in range(0, numbers_count - 1):
        index_of_min = i

        for j in range(i + 1, numbers_count):
            if numbers[j] < numbers[index_of_min]:
                index_of_min = j
        
        temp = numbers[index_of_min]
        numbers[index_of_min] = numbers[i]
        numbers[i] = temp

    return numbers


def sort_with_swap_check(numbers, numbers_count):
    """If table is mostly sorted or replacement cost is high, we can add 
    elements swap check. Replacements - min Θ(1), max Θ(numbers_count - 1) 
    
    >>> numbers =  [8, 6, 7, 4, 5, 2, 3, 1]
    >>> numbers_count = 8
    >>> sort(numbers, numbers_count)
    [1, 2, 3, 4, 5, 6, 7, 8]
    """

    for i in range(0, numbers_count - 1):
        index_of_min = i

        for j in range(i + 1, numbers_count):
            if numbers[j] < numbers[index_of_min]:
                index_of_min = j
        
        if index_of_min != i:
            temp = numbers[index_of_min]
            numbers[index_of_min] = numbers[i]
            numbers[i] = temp

    return numbers
