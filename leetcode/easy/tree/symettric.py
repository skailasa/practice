"""
Given a binary tree, check whether it is a mirror of itself
(ie, symmetric around its center).
"""


class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


def check_symettric(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        if root1.val == root2.val:
            return (check_symettric(root1.left, root2.right) and
                    check_symettric(root1.right, root2.left))

    return False


def check_symettric_wrapper(root):
    return check_symettric(root, root)


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

    print(check_symettric_wrapper(n2))