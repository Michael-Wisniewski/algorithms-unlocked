def compress_test(text):
    """
    >>> text = 'TATAGATCTTAATATA'
    >>> compress_test(text)
    [84, 65, 256, 71, 257, 67, 84, 256, 257, 264]
    """
    dictionary = []
    compressed_text = []

    for i in range(256):
        dictionary.append(chr(i))

    s = text[0]

    for i in range(1, len(text)):
        c = text[i]

        if s + c in dictionary:
            s = s + c
        else:
            index = dictionary.index(s)
            compressed_text.append(index)
            dictionary.append(s + c)
            s = c

    index = dictionary.index(s)
    compressed_text.append(index)

    return compressed_text


