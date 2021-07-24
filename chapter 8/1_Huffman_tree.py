def build_huffman_tree(characters, frequencies, n):
    """Time complexity: O(n lg n), where n is number of uncompressed characters.

    >>> characters = ['T', 'C', 'G', 'A']
    >>> frequencies = [0.45, 0.05, 0.05, 0.45]
    >>> n = 4
    >>> build_huffman_tree(characters, frequencies, n)
    {'freq': 1.0, '0': {'char': 'A', 'freq': 0.45}, '1': {'freq': 0.55, '0': {'freq': 0.1, '0': {'char': 'C', 'freq': 0.05}, '1': {'char': 'G', 'freq': 0.05}}, '1': {'char': 'T', 'freq': 0.45}}}
    """
    Q = []

    for i in range(n):
        z = {
           'char': characters[i],
           'freq': frequencies[i]
        }
        Q.append(z)

    for i in range(n - 1):
        x = get_min(Q)
        y = get_min(Q)

        z = {
            'freq': x['freq'] + y['freq'],
            '0': x,
            '1': y
        }

        Q.append(z)

    return Q[0]

def get_min(Q):
    min_leaf_index = 0

    for i in range(1, len(Q)):
        if Q[i]['freq'] < Q[min_leaf_index]['freq']:
            min_leaf_index = i
    
    min_leaf = Q.pop(min_leaf_index)

    return min_leaf
