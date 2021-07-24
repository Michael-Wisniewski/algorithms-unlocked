from math import floor


def build_huffman_tree(characters, frequencies, n):
    """Time complexity: O(n lg n), where n is number of uncompressed characters.

    >>> characters = ['A', 'C', 'G', 'T']
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
        append_to_heap(Q, z)

    for i in range(n - 1):

        x = pop_min_from_heap(Q)
        y = pop_min_from_heap(Q)

        z = {
            'freq': x['freq'] + y['freq'],
            '0': x,
            '1': y
        }

        append_to_heap(Q, z)

    return Q[0]

def append_to_heap(Q, z):
    """Time complexity: O(lgn), n - number of heap's elements.

    >>> Q = [{'char': 'C', 'freq': 0.05}, {'char': 'A', 'freq': 0.45}, {'char': 'T', 'freq': 0.45}]
    >>> z = {'char': 'G', 'freq': 0.05}
    >>> append_to_heap(Q, z)
    >>> Q
    [{'char': 'C', 'freq': 0.05}, {'char': 'G', 'freq': 0.05}, {'char': 'T', 'freq': 0.45}, {'char': 'A', 'freq': 0.45}]
    """
    Q.append(z)
    element_index = len(Q) - 1
    parent_index = floor((element_index - 1) / 2)

    while element_index != 0 and Q[parent_index]['freq'] > Q[element_index]['freq']:
        temp = Q[parent_index]
        Q[parent_index] = Q[element_index]
        Q[element_index] = temp

        element_index = parent_index
        parent_index = floor((element_index - 1) / 2)

def pop_min_from_heap(Q):
    """Time complexity: O(lgn), n - number of heap's elements.

    >>> Q = [{'char': 'C', 'freq': 0.05}, {'char': 'G', 'freq': 0.05}, {'char': 'T', 'freq': 0.45}, {'char': 'A', 'freq': 0.45}]
    >>> pop_min_from_heap(Q)
    {'char': 'C', 'freq': 0.05}
    >>> Q
    [{'char': 'G', 'freq': 0.05}, {'char': 'A', 'freq': 0.45}, {'char': 'T', 'freq': 0.45}]
    """
    if len(Q) == 1:
        return Q.pop(0)

    u = Q[0]
    last_index = len(Q) - 1
    Q[0] = Q.pop(last_index)
    last_index -= 1

    element_index = 0

    while True:
        left_child_index = 2 * element_index + 1
        right_child_index = 2 * element_index + 2

        if (
            right_child_index <= last_index and 
            Q[right_child_index]['freq'] < Q[element_index]['freq'] and
            Q[right_child_index]['freq'] < Q[left_child_index]['freq']
        ):
            temp = Q[element_index]
            Q[element_index] = Q[right_child_index]
            Q[right_child_index] = temp
            element_index = right_child_index
        elif (
            left_child_index <= last_index and
            Q[left_child_index]['freq'] < Q[element_index]['freq']
        ):
            temp = Q[element_index]
            Q[element_index] = Q[left_child_index]
            Q[left_child_index] = temp
            element_index = left_child_index
        else:
            break

    return u
