"""
Given a sorted, increasing order, array with *unique* integer
elements write an algorithm to crate a binary tree with minimal
height.
"""


class Node:

    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return str(
            {
                "val": self.val,
                "left": self.left,
                "right": self.right,
            }
        )


class Tree:

    def find_root(self, A):
        idx = len(A)//2
        return A[idx]

    def minimal(self, A):

        if len(A):
            root = self.find_root(A)

            node = Node(root)

            midpoint = len(A)//2

            left_A = A[:midpoint]
            right_A = A[midpoint+1:]

            node.left = self.minimal(left_A)
            node.right = self.minimal(right_A)

            return node

        return


if __name__ == "__main__":
    A = [1,2,3,4]
    t = Tree()

    print(t.minimal(A))

