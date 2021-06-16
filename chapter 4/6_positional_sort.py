def code_tickets_number(ticket_numbers):
    parsed_codes = []

    for ticket_code in ticket_numbers:
        parsed_code = []

        for char in ticket_code:
            char_num = ord(char)

            if char_num >= 65:
                char_num -= 54
            else:
                char_num -= 48

            parsed_code.append(char_num)
        parsed_codes.append(parsed_code)
    return parsed_codes


def decode_tickets_number(ticket_numbers):
    parsed_codes = []

    for ticket_code in ticket_numbers:
        parsed_code = ""

        for char_num in ticket_code:

            if char_num >= 11:
                char_num += 54
            else:
                char_num += 48

            parsed_code += chr(char_num)
        parsed_codes.append(parsed_code)
    return parsed_codes


def count_equal_keys(A, n, k):
    equal_keys = [0] * 36

    for i in range(0, n):
        index = A[i][k]
        equal_keys[index] += 1

    return equal_keys


def count_smaller_keys(equal_keys, n, k):
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


def sort_by_character(A, n, k):
    equal_keys = count_equal_keys(A, n, k)
    smaller_keys = count_smaller_keys(equal_keys, n, k)
    return reorganize(A, smaller_keys, n, k)


def sort(ticket_numbers, tickets_count, code_length):
    """Time complexity: Θ(n)."""
    coded_tickets = code_tickets_number(ticket_numbers)

    for k in range((code_length - 1), -1, -1):
        sorted_tickets = sort_by_character(coded_tickets, tickets_count, k)

    return decode_tickets_number(sorted_tickets)


ticket_numbers = ["X3", "F3", "T2"]
tickets_count = 3
code_length = 2

sorted_tickets = sort(ticket_numbers, tickets_count, code_length)
print("Sorted tickets:", sorted_tickets)
