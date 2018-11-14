"""
QuickSort implementation

Divide: Partition (rearrange) the array A[low...high] into two 
possibly empty sub-arrays s.t. all in array below pivot leq to
pivot, and pivot leq to all in array above pivot.


Conquer: Sort two subarrays above and below pivot by recursive
calls to quicksort.

Partition is key to procedure: see diagram on p 172 of CLRS for details
- 

"""


class Quick:

    def partition(self, A, low, high):
        pivot = A[high]
        i = low - 1
        for j in range(low, high):
            if A[j] <= pivot:
                i += 1
                A[i], A[j] = A[j], A[i]

        A[i + 1], A[high] = A[high], A[i + 1]

        return i + 1

    def sort(self, A, low, high):
        if low < high:
            p = self.partition(A, low, high)
            self.sort(A, low, p - 1)
            self.sort(A, p + 1, high)


if __name__ == "__main__":
    A = [5, 4, 3, 2, 1]
    Quick().sort(A, 0, 4)
    print(A)
