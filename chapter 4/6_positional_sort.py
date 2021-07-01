def positional_sort(tickets, tickets_num, code_length):
    """Time complexity: Θ(n), Ω(n) if m is constant, memory consumption - Θ(n), Ω(n).
    
    >>> tickets = ['A4', '0A', 'A2', 'BB']
    >>> tickets_num = 4
    >>> code_length = 2
    >>> positional_sort(tickets, tickets_num, code_length)
    ['0A', 'A2', 'A4', 'BB']
    """
    coded_tickets = code_tickets_number(tickets)
    sorted_tickets = coded_tickets

    for k in range((code_length - 1), -1, -1):
        sorted_tickets = sort_by_character(sorted_tickets, tickets_num, k)

    return decode_tickets_number(sorted_tickets)

def sort_by_character(A, n, k):
    equal_keys = count_equal_keys(A, n, k)
    smaller_keys = count_smaller_keys(equal_keys, k)
    return reorganize(A, smaller_keys, n, k)

def count_equal_keys(A, n, k):
    equal_keys = [0] * 36

    for i in range(0, n):
        index = A[i][k]
        equal_keys[index] += 1

    return equal_keys

def count_smaller_keys(equal_keys, k):
    smaller_keys = [0] * 36

    for i in range(1, 36):
        smaller_keys[i] = smaller_keys[i - 1] + equal_keys[i - 1]

    return smaller_keys

def reorganize(A, smaller_keys, n, k):
    B = [0] * n
    subsequent = [0] * 36

    for j in range(0, 36):
        subsequent[j] = smaller_keys[j] + 1

    for i in range(0, n):
        key = A[i][k]
        index = subsequent[key]
        B[index - 1] = A[i]
        subsequent[key] += 1

    return B

def code_tickets_number(tickets):
    parsed_codes = []

    for ticket_code in tickets:
        parsed_code = []

        for char in ticket_code:
            char_num = ord(char)

            if char_num >= 65:
                char_num -= 55
            else:
                char_num -= 48

            parsed_code.append(char_num)
        parsed_codes.append(parsed_code)
    return parsed_codes


def decode_tickets_number(tickets):
    parsed_codes = []

    for ticket_code in tickets:
        parsed_code = ""

        for char_num in ticket_code:

            if char_num >= 10:
                char_num += 55
            else:
                char_num += 48

            parsed_code += chr(char_num)
        parsed_codes.append(parsed_code)
    return parsed_codes
