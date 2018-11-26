"""
Write a program to swap odd an even bits in an integer with as few
    instructions as possible.
    e.g. bit 0 and 1 are swapped, bit 2 and 3 are swapped and so on.
"""


def swap(x):

    # Get all even bits of x
    even_bits = x & 0xAAAAAAAA

    # Get all odd bits of x
    odd_bits = x & 0x55555555

    # Right shift even bits
    even_bits >>= 1

    # Left shift odd bits
    odd_bits <<= 1

    # Combine even and odd bits
    return (even_bits | odd_bits)


if __name__ == '__main__':

    num = 123
    print(bin(num))

    print(swap(num))