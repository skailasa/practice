"""
Binary trees, and basic traversal methods. These tree traversal methods
    are a cases of Depth-First search.
"""


class Node:
    """Simple node class for binary tree"""
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.visited = False

    def visit(self):
        self.visited = True


def in_order_traversal(node):
    """
    In order traversal, left branch visited before node, followed by
        right branch. Hence in order.
    """
    if node:
        in_order_traversal(node.left)
        print(node.name)
        node.visit()
        in_order_traversal(node.right)


def pre_order_traversal(node):
    """
    Pre-order traversal, root visited before children
    """
    if node:
        node.visit()
        print(node.name)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def post_order_traversal(node):
    """
    Post-order traversal, children visited before root.
    """
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.name)
        node.visit


if __name__ == "__main__":
    n2 = Node(2)
    n1 = Node(1)
    n3 = Node(3)

    # construct simple BST
    n2.left = n1
    n2.right = n3

    in_order_traversal(n2)  # expected: 1, 2, 3

    pre_order_traversal(n2)  # expected: 2, 1, 3

    post_order_traversal(n2)  # expected: 1, 3, 2
