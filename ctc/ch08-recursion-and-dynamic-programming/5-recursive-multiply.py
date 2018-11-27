"""
Write a recursive function to multiply two positive integers without
    using the * operator.
    You can use addition, subtraction, and bit shifting, but you should
    minimise the number of those operations.
"""


def mult(m, n):

    if n == 0:
        return 0

    elif n == 1:
        return m

    else:
        res = m + mult(m, n-1)

    return res


if __name__ == "__main__":

    a, b = 3, 3

    print(mult(a, b))