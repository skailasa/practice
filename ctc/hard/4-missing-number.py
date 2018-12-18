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


def find_missing_integer(l):
    n = len(l)
    expected = n*(n+1)/2
    found = 0

    for num in l:
        if num is not None:
            found += num

    print(expected-found)


if __name__ == "__main__":

    l = [1, 2, 3, 5]  # separated from missing number by 2^2

    find_missing_integer(l)


