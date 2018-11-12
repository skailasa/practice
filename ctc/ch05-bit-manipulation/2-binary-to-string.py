"""
Given a real number between 0 and 1 [0, 1) that is passed in as a double
print the binary representation. If the number cannot be represented
accurately in binary with at most 32 characters you must print "ERROR"
"""


class Binary:
    """
    Convert a double into a binary string
    """

    def __init__(self, n):
        self.n = n
        self.bin = '0.'
        self.counter = 0
        self.precision = 32

    def __repr__(self):
        self._binary(self.n)

        return str(self.bin)

    def _binary(self, n):
        while self.counter <= self.precision:
            if n*2 >= 1:
                self.counter += 1
                self.bin += '1'
                temp = abs(1-n*2)
                self._binary(temp)

            else:
                self.counter +=1
                self.bin += '0'
                self._binary(n*2)
                self.counter += 1


if __name__ == "__main__":
    print(Binary(0.875))



