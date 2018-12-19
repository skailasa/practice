"""
An array A contains all the integers from 0 to n, except for one number
    which is missing.

In this problem, we cannot access an entire integer in A with a single
    operation. The elements of A are represented in binary, and the only
    operation we can use is fetch the jth bit of A[i] which takes constant
    time.

Write code to find the missing integer.
Can you do this in O(N) time?

"""


def missing_integer_simple(l):
    """
    Compute in a simple way, but O(NLog(N)) complexity
    """
    n = len(l)-1
    expected = n*(n+1)/2
    found = 0

    for num in l:
        if num is not None:
            found += num

    print(expected-found)


def count(l, shift=0):
    c = {0: 0, 1: 0}

    for n in l:
        if bin(n >> shift)[-1] == '0':
            c[0] += 1
        elif bin(n >> shift)[-1] == '1':
            c[1] += 1

    return c


def missing_integer(l, shift):

    c = count(l[0], shift)
    missing_int = ''
    even = False
    print(c)
    if l[1] % 2 == 0:
        even = True

    if even:
        # If the list is of even length expect equal number of 0s and 1s
        if c[0] == c[1] + 1:
            # a one is missing, meaning that the missing integer is odd
            missing_int += '1'
        elif c[1] == c[0] + 1:
            # a zero is missing, meaning that the missing integer is even
            missing_int += '0'

    else:
        # If the list is of odd length, expect #0s = #1s + 1
        if c[0] == c[1]:
            # a zero is missing
            missing_int += '0'

        elif c[0] == c[1] + 2:
            # a one is missing
            missing_int += '1'

    return missing_int


def filter_evens(l, shift):
    res = []
    for n in l:
        if bin(n >> shift)[-1] == '0':
            res.append(n)

    return res


def filter_odds(l, shift):
    res = []
    for n in l:
        if bin(n >> shift)[-1] == '1':
            res.append(n)
    return res


if __name__ == "__main__":

    # a six is missing, 110 in binary
    l = ([0, 1, 2, 3, 4, 5], 7)
    print(missing_integer(l, 0))
    # should output 0, therefore filter out odds
    print(filter_evens(l[0], 0))
    # results in [0, 2], put this back into algorithm
    print(missing_integer(([0, 4, 2], 4), 1))
    # results in 1, filter out evens [2]
    print(filter_odds([0, 4, 2], 1))
    print(missing_integer(([2], 2), 2))
