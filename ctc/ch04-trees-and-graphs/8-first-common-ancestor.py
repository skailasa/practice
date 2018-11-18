"""
Design an algorithm to find the first common ancestor of two nodes of a
    binary tree.
    Avoid storing additional nodes in a data structure
    NOTE: This is not necessarily a binary search tree.
"""


class TreeNode:
    """Simple node class for binary tree"""
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.parent = None


def check_ancestor(ancestor, node):
    """
    Check whether a given node is another node's ancestor by recursing
        up the binary tree.
    """
    if ancestor.name == node.name:
        return True

    else:
        if node.parent:
            return check_ancestor(ancestor, node.parent)
        else:
            return False


def check_common_ancestor(common_ancestor, node1, node2):
    """
    For two nodes, check whether they share a given common ancestor using
        the check_ancestor function.
    """
    if (check_ancestor(common_ancestor, node1) and
            check_ancestor(common_ancestor, node2)):

        return True

    return False


def first_common_ancestor(node1, node2):
    """
    We can easily adapt check_common_ancestor to find the first common
        ancestor, we check if the left node's parent is a common ancestor
        otherwise we recurse up to the next layer, checking whether this
        is a common ancestor, stopping when we've found a common ancestor.
    """
    if node1.parent:
        if check_common_ancestor(node1.parent, node1, node2):
            return node1.parent.name
        else:
            first_common_ancestor(node1.parent, node2)


if __name__ == "__main__":
    n2 = TreeNode(2)
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)

    # construct simple BST
    n2.left = n1
    n2.right = n3

    n1.parent = n2
    n3.parent = n2

    n3.right = n4
    n4.parent = n3

    n4.right = n6
    n5.left = n5
    n5.parent = n4
    n6.parent = n4

    #check_common_ancestor(n2, n1, n5)

    print(first_common_ancestor(n5, n6))
