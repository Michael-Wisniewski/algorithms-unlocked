def decompress_test(compressed_text):
    """
    >>> compressed_text = [84, 65, 256, 71, 257, 67, 84, 256, 257, 264]
    >>> decompress_test(compressed_text)
    'TATAGATCTTAATATA'
    """
    dictionary = []
    decompressed_text = []

    for i in range(256):
        dictionary.append(chr(i))

    current_index = compressed_text[0]
    decompressed_text.append(dictionary[current_index])

    for i in range(1, len(compressed_text)):
        previous_index = current_index
        current_index = compressed_text[i]

        if current_index < len(dictionary):
            s = dictionary[current_index]
            decompressed_text.append(s)
            c = dictionary[previous_index]
            dictionary.append(c + s[0])
        else:
            s = dictionary[previous_index] + dictionary[previous_index][0]
            decompressed_text.append(s)
            dictionary.append(s)

    return ''.join(decompressed_text)
