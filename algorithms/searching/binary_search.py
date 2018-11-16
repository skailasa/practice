"""
Implementation of Binary Search
"""


class Binary:
    def __init__(self, A):
        self.A = A

    def iterative_search(self, x):
        start = 0
        end = len(self.A)

        while start < end:
            mid = int((start + end) / 2)
            if self.A[mid] < x:
                start = mid + 1
            elif self.A[mid] > x:
                end = mid
            else:
                return mid

    def recursive_search(self, x, start, end):
        mid = int((start + end) / 2)

        if self.A[mid] < x:
            return self.recursive_search(x, mid + 1, end)

        elif self.A[mid] > x:
            return self.recursive_search(x, start, mid - 1)

        else:
            return mid


if __name__ == "__main__":
    x = 10
    A = [1, 2, 10, 100, 1312]

    print(Binary(A).iterative_search(x))

    print(Binary(A).recursive_search(x, 0, 4))
