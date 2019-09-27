"""
Heaps are like binary trees, can be composed of arrays.

Max heaps: Parent node => children
Min heaps: vice versa

Can define Left and Right methods on Heaps, easy to implement with
bitwise operators.
"""


def parent(i):
    return (i-1) >> 1


def left(i):
    return ((i+1) << 1) - 1


def right(i):
    return (i+1) << 1


def max_heapify(H, i):
    """Maintains max heap property"""
    l = left(i)
    r = right(i)
    if l <= H.heap_size and H[l] > H[i]:
        largest = l
    else:
        largest = i

    if r <= H.heap_size and H[r] > H[largest]:
        largest = r

    if largest != i:
        tmp = H[i]
        H[i] = H[largest]
        H[largest] = tmp
        max_heapify(H, largest)


def build_max_heap(H):

    for i in range(H.length//2 - 1, -1, -1):
        max_heapify(H, i)


class Heap:

    def __init__(self, A):
        self.A = A
        self.heap_size = len(A)
        self.length = len(A)

    def __getitem__(self, item):
        return self.A[item]

    def __setitem__(self, key, value):
        self.A[key] = value

    def __repr__(self):
        return str(self.A)


if __name__ == "__main__":
    A = [6, 4, 7, 1, 5, 10, 0]

    H = Heap(A)
    build_max_heap(H)

    print(H)
