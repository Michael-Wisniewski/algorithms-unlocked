from math import floor

def search(letters, letters_num, wanted_letter):
    """Time complexity - lg(n), memory consumption - O(n)
    
    List contains wanted letter.
    >>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    >>> letters_num = 8
    >>> wanted_letter = 'g'
    >>> search(letters, letters_num, wanted_letter)
    6

    List without wanted letter.
    >>> letters = ['a', 'b', 'c', 'd']
    >>> letters_num = 4
    >>> wanted_letter = 'x'
    >>> search(letters, letters_num, wanted_letter)
    False
    """

    p = 0
    r = letters_num - 1

    while p <= r:
        q = floor((p + r) / 2)

        if letters[q] == wanted_letter:
            return q
        elif letters[q] > wanted_letter:
            r = q - 1
        else:
            p = q + 1

    return False
