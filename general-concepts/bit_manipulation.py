"""
The following operations are very important to understand
the implementation of
"""


def get_bit(num, i):
    """
    Shifts 1 over by i bits, by performing an & with num we
        clear all bits other than the bit at i. Finally compare
        that to 0, if it is zero that's what we have, otherwise
        we have 1.
    """
    if ((1 << i) & num == 0):
        return 0
    return 1


def set_bit(num, i):
    """
    Shifts 1 over by i bits, performs an | with num, only the value
        at i will change to a 1 if it is 0, every other value will
        take | with 0 keeping it the same.
    """
    return (1 << i) | num


def clear_bit(num, i):
    """
    Need to create a number like 1111101111 where the number in the
        same position of 0 will be & with and therefore erased
    """
    mask = ~(1 << i)
    return num & mask


def all_ones(num):
    """
    Check if a number in binary contains all ones
    """
    return ((num + 1) & num == 0) and (num != 0)


def one_followed_by_zeros(num):
    """
    Check if a number is consists of a leading one, followed by zeros
        in binary representation.
    """
    return (num & (num-1)) == 0
