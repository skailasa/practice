"""
Given two standard arrays A and B
- A has a large enough buffer at the end to hold B
- Write a method to merge B into A in sorted order
"""


class Sorted:

    def __init__(self, A, B):
        """init with two sorted arrays"""
        self.A = A
        self.B = B

    def merge(self):
        """Take inspiration from merge sort"""
        A_idx, B_idx = 0, 0
        result = []

        while A_idx < len(self.A) and B_idx < len(self.B):
            if self.A[A_idx] < self.B[B_idx]:
                result.append(self.A[A_idx])
                A_idx += 1
            elif self.A[A_idx] > self.B[B_idx]:
                result.append(self.B[B_idx])
                B_idx +=1

        result += self.A[A_idx:]
        result += self.B[B_idx:]

        return result


if __name__ == "__main__":
    A = [1, 2, 3, 4]
    B = [5, 6, 7, 8]
    r = Sorted(A, B).merge()
    print(r)