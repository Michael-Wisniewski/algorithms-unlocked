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
 
    last_index = names_num - 1
    temp = names[last_index]
    names[last_index] = wanted_name

    i = 0
    while names[i] != wanted_name:
        i += 1

    names[last_index] = temp

    if i < last_index or names[last_index] == wanted_name:
        return i
    else:
        return False
