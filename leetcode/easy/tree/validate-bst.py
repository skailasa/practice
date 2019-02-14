"""
Validate a binary search tree

Strategy, the root must always be greater than or equal to it's left
substree, and less than or equal to its right substree's values.
"""


class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


def validate_bst(root, _min=-10000, _max=10000):

    # empty bst is valid
    if root is None:
        return True

    elif root.val < _min or root.val > _max:
        return False

    else:
        return (
            validate_bst(root.left, _min, root.val-1) and
            validate_bst(root.right, root.val+1, _max)
        )


if __name__ == "__main__":
    n2 = Node(2)
    n1 = Node(1)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    # construct simple BST
    n2.left = n1
    n2.right = n3
    n3.right = n4
    n4.right = n5

    #print(n1.height)

    print(validate_bst(n2))

