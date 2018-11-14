import collections


class Bucket:

    def insertion_sort(self, A):

        for i in range(1, len(A)):
            key = A[i]
            j = i - 1

            while 0 <= j and A[j] > key:  # remember A[i] to the right of A[j]

                A[j + 1] = A[j]  # if this is the case we move A[j] to A[j+1], where the key was

                j -= 1  # until we get to the very left of the array
            # at this point j should be equal to 1 below the correct index for the key as everything
            # below this (to the left) will be less than the key causing us to exit the while loop
            # and leading the assignment in the following line
            A[j + 1] = key
        return A

    def sort(self, A):
        n = len(A)
        buckets = collections.defaultdict(list)

        for i in range(n):
            buckets[int(n * A[i])].append(A[i])

        for k, v in buckets.items():
            buckets[k] = self.insertion_sort(v)

        return buckets


if __name__ == "__main__":
    # print(Bucket().sort([0.143,0.132,0.41]))
    print(Bucket().insertion_sort([50, 1, 2, 3, 4, 5]))
