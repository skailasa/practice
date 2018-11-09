"""
Insertion. Two 32 bit numbers: N, M.
Two bit positions, i and j.
Write a method to insert M into N s.t. M starts at bit j
and ends at bit i.
Assumption: bits j through i have enough space to fit all
of M.

e.g. N = 10000 i, j = 3, i = 1 M = 11
     N = 10110
"""


def clear_bit(N, i):
    """
    Create a mask to clear a bit at position i
        Works by shifting 1 along i bits, and negating.
        creating a bin number like 11110111 with a 0 in
        the position we want to clear.
        Taking an and with our target N will lead to the
        bit at position i being cleared.
    """

    mask = ~(1 << i)
    N &= mask
    return N


class Insert:
    """Insert one number into another"""

    def __init__(self, N, i, j):
        """Initialise with N, i and j"""
        self.N = N
        self.i = i
        self.j = j

    def insert(self, M):
        """
        Strategy:
            - clear all bits where M is to go
            - shift M up by i (logical shift)
            - take an OR between N and M
                - remember OR with 0 operates like identity
        """
        # clear all bits between i and j
        for idx in range(self.i, self.j):
            self.N = clear_bit(self.N, idx)

        # shift M up to where it should be inserted
        M = M << self.i

        # take an OR between N and M
        result = self.N | M

        return bin(result), bin(self.N), bin(M)


if __name__ == "__main__":
    N = 15
    M = 2
    i, j = 1, 3

    print(Insert(N, i, j).insert(M))