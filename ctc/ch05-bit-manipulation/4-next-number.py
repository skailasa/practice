"""
Given a positive integer, print the next smallest and next largest number
    that have the same number of 1 bits in their binary representation.
"""


def check_current_bit_1(num):
    if (num & 1) & 1 == 1:
        return True
    return False


def set_bit(num, i):

    return num | (1 << i)


def clear_bit(num, i):
    mask = ~ (1 << i)
    return num & mask


def all_ones(num):
    return ((num+1) & num == 0) and (num != 0)


def get_next_largest(num):

    idx = 0
    found = False
    original_num = num

    if all_ones(num):
        return bin(2*num)

    while not found:
        idx += 1
        if check_current_bit_1(num) and not check_current_bit_1(num >> 1):
            found = True
        num = num >> 1

    # set 0
    original_num = set_bit(original_num, idx)
    # clear 1
    original_num = clear_bit(original_num, idx-1)

    return bin(original_num)


def get_next_smallest(num):
    idx = 0
    found = False
    original_num = num

    if all_ones(num):
        return "Not Possible"

    while not found:
        idx += 1
        if not check_current_bit_1(num) and check_current_bit_1(num >> 1):
            found = True
        num = num >> 1

    # set 0
    original_num = clear_bit(original_num, idx)
    # clear 1
    original_num = set_bit(original_num, idx-1)

    return bin(original_num)


if __name__ == "__main__":
    num = 15
    print(bin(num))
    print('h', get_next_largest(num))
    print(get_next_smallest(num))