"""
A magic index is defined as such that in A[i] = i. Given a sorted array
    of distinct integers, write a method to find a magic index, if one
    exists in A.

    Follow Up: What if the values aren't distinct?

"""


def find_magic_index(A):
    """
    If values are distinct
    """

    mid = len(A) // 2
    if A[mid] == mid:
        print(mid)

    elif A[mid] > mid:
        find_magic_index(A[:mid])

    else:
        find_magic_index(A[mid:])


CHECKED_IDXS = []


def find_magic_index_indistinct(A, idx):
    """
    If values in array are indistinct.
    """

    global CHECKED_IDXS

    if idx not in CHECKED_IDXS:

        if A[idx] > idx:
            CHECKED_IDXS.extend([i for i in range(idx, A[idx])])
            find_magic_index_indistinct(A, A[idx])

        elif A[idx] == idx:
            print(A[idx])
            return

        else:
            CHECKED_IDXS.append(idx)
            find_magic_index_indistinct(A, idx+1)

    return


if __name__ == "__main__":

    A = [2, 3, 4, 4, 5, 6, 7, 7]
    # A = [-1, -1, -1, 3]

    find_magic_index_indistinct(A, 0)
