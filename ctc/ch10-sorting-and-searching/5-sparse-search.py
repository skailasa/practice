"""
Given a sorted array of strings that is interspersed with empty strings,
write a method to find the location of a given string.

input: ['a', '', '', 'b', '', '', '', 'c'] find 'c'
output: 7
--
Strategy:
    - modify binary search
    - find first non empty string near middle and make
    this the mid point
    - after this can implement binary search
"""


def binary_search(x, A, start, end):

    mid = int((start + end) / 2)

    if not A[mid]:
        left = mid - 1
        right = mid + 1
        while True:
            if left < start and right > end:
                return
            elif right <= end and A[right]:
                mid = right
                break
            elif left >= start and A[left]:
                mid = left
                break

            left -= 1
            right += 1

    if x == A[mid]:
        print(mid)
        return mid

    elif x < A[mid]:
        binary_search(x, A, start, mid-1)

    elif x > A[mid]:
        binary_search(x, A, mid+1, end)


if __name__ == "__main__":
    binary_search('d', ['a', '', '', 'b', 'c', '', '', 'd'], 0, 7)
