from math import floor


def sort_with_binary_heap(A, n):
    """Time complexity: O(nlgn), n - number of elements.

    >>> numbers = [4, 7, 9, 2, 8, 3, 5, 2, 1, 5, 9]
    >>> numbers_count = 11
    >>> sort_with_binary_heap(numbers, numbers_count)
    [1, 2, 2, 3, 4, 5, 5, 7, 8, 9, 9]
    """
    Q = build_heap(A, n)
    sorted_list = []

    for _ in range(n):
        minimal_value = pop_min_from_heap(Q)
        sorted_list.append(minimal_value)
        
    return sorted_list

def pop_min_from_heap(Q):
    """Time complexity: O(lgn), n - number of elements.

    >>> Q = [2, 4, 9, 7]
    >>> pop_min_from_heap(Q)
    2
    >>> Q
    [4, 7, 9]
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
            Q[right_child_index] < Q[element_index] and
            Q[right_child_index] < Q[left_child_index]
        ):
            temp = Q[element_index]
            Q[element_index] = Q[right_child_index]
            Q[right_child_index] = temp
            element_index = right_child_index
        elif (
            left_child_index <= last_index and
            Q[left_child_index] < Q[element_index]
        ):
            temp = Q[element_index]
            Q[element_index] = Q[left_child_index]
            Q[left_child_index] = temp
            element_index = left_child_index
        else:
            break

    return u

def build_heap(A, n):
    """Time complexity: O(nlgn), n - number of elements.

    >>> numbers = [4, 7, 9, 2]
    >>> numbers_count = 4
    >>> build_heap(numbers, numbers_count)
    [2, 4, 9, 7]
    """
    Q = []

    for index in range(n):
        Q.append(A[index])
        element_index = index
        parent_index = floor((element_index - 1) / 2)

        while element_index != 0 and Q[parent_index] > Q[element_index]:
            temp = Q[parent_index]
            Q[parent_index] = Q[element_index]
            Q[element_index] = temp

            element_index = parent_index
            parent_index = floor((element_index - 1) / 2)

    return Q
