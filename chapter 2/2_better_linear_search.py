def search(names, names_num, wanted_name):
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
 
    i = 0

    while i < names_num:
        if names[i] == wanted_name:
            return i
        i += 1

    return False
