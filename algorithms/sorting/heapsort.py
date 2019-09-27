from datastructures.heap import Heap, build_max_heap, max_heapify


def heap_sort(H):
    build_max_heap(H)
    for i in range(H.length-1, 0, -1):
        tmp = H[0]
        H[0] = H[i]
        H[i] = tmp
        H.heap_size -= 1
        max_heapify(H, 0)


h = Heap([4,5,6,1,2,3])

heap_sort(h)

print(h)
