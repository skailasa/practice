"""
Given a sorted array of n integers that has been rotated an unknown
number of times, write code to find an element in the array. You may
assume that the array was originally sorted in increasing order.

e.g. find 5 in [15, 16, 19, 20, 25, 1, 3, 5, 6, 7, 10]

outputs 7
-
Strategy:
    - we know the original array was sorted in increasing order,
        - so if there is a negative diff between consecutive elements this
        was where the array originally started.
"""


def binary_search(x, A):

    start = 0
    end = len(A)

    while start < end:
        mid = int((end+start)/2)
        if x < A[mid]:
            end = mid
        elif x > A[mid]:
            start = mid+1
        else:
            return mid


def find_element(x, A_rotated):
    """Of complexity O(log(n) + n) = O(log(n))"""
    pivot = 0

    for i in range(len(A_rotated)-1):
        if A_rotated[i+1] - A_rotated[i] < 0:
            pivot = i
            break

    if A[0] <= x < A[pivot]:
        return binary_search(x, A_rotated[:pivot])

    return binary_search(x, A_rotated[pivot:]) + pivot


if __name__ == "__main__":
    A = [15, 16, 19, 20, 25, 1, 3, 5, 6, 7, 10]
    print(find_element(5, A))


