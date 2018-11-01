"""
Implementation of Merge Sort
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
    A = [5,4,3,2,1]

    print(Merge().sort(A))