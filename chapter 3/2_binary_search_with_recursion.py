from math import floor

def search(letters, p, r, wanted_letter):
    """Time complexity - lg(n), memory consumption - O(n)
    
    List contains wanted letter.
    >>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    >>> p = 0
    >>> r = 7
    >>> wanted_letter = 'g'
    >>> search(letters, p, r, wanted_letter)
    6

    List without wanted letter.
    >>> letters = ['a', 'b', 'c', 'd']
    >>> p = 0
    >>> r = 3
    >>> search(letters, p, r, wanted_letter)
    False
    """

    if p > r:
        return False
    
    q = floor((p + r) / 2)
    
    if letters[q] == wanted_letter:
        return q
    elif letters[q] > wanted_letter:
        return search(letters, p, q - 1, wanted_letter)
    else:
        return search(letters, q + 1, r, wanted_letter)
