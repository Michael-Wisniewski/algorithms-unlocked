def search(names, names_num, wanted_name, index=0):
    """Time complexity - O(n), memory consumption - O(n)

    List contains wanted name.
    >>> names = ['Paul', 'Dennis', 'Gregory', 'Nathan', 'Scott', 'Julian', 'Miles', 'Laura']
    >>> names_num = 8
    >>> wanted_name = 'Scott'
    >>> search(names, names_num, wanted_name)
    4
    
    List without wanted name.
    >>> names = ['Paul', 'Dennis', 'Gregory', 'Nathan']
    >>> names_num = 4
    >>> wanted_name = 'Adam'
    >>> search(names, names_num, wanted_name)
    False
    """

    if index > (names_num - 1):
        return False
    elif names[index] == wanted_name:
        return index
    else:
        return search(names, names_num, wanted_name, index + 1)
