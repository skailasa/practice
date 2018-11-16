"""
Implementation of Merge Sort.

Analysis (CLRS):
- Each divide step yields two subsequences of size n/2
- Merge sort of just one element is constant time

- Divide Step: Computes the middle of the array
               takes constant time.
- Conquer Step: Recursively solve two subproblems of size n/2
                - 2T(n/2) runtime where T(n) is runtime for whole array sort
- Combine Step: Merge procedure is O(N)

can infer that there are log(N) + 1 levels to recursion tree inductively.
Consider a list of length 1, log(1) + 1 = 1. So we only recursively call
the algorithm once.
Furthermore, each level takes O(N) work to merge.
So total runtime complexity can be seen to be \kappaN(log(N) + 1)== O(NlogN)
"""


class Merge:

    def merge(self, left, right):
        left_index, right_index = 0, 0
        result = []

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result += left[left_index:]
        result += right[right_index:]

        return result

    def sort(self, array):
        if len(array) <= 1:  # base case
            return array

        # divide array in half and merge sort recursively
        half = len(array) // 2
        left = self.sort(array[:half])
        right = self.sort(array[half:])

        return self.merge(left, right)


if __name__ == "__main__":
    A = [5, 4, 3, 2, 1]

    print(Merge().sort(A))