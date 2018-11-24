"""
T1 and T2 are two very large Binary Trees, T1 >> T2 though. Create an
    algorithm to check if T2 is a subtree of T1. i.e. if you cut off the
    tree from a given node in T1 that would be T2.

Strategy:
    - Recursively check for whether the condition is not satisfied.
    - look through T1 for T2.root
        - if found then check children recursively making the same
        comparison.
"""


class TreeNode:
    """Simple node class for binary tree"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


def find_x(t1, x):
    """
    Function to find an element x in a binary tree with a root at t1
        iteratively.
    """

    if not t1:
        return False

    queue = list()
    queue.append(t1)

    while queue:
        node = queue[-1]
        queue.pop()
        if node.data == x:
            return node

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return None


EQUAL = False


def check_equal_trees(t1, t2):
    """
    Function to check whether two trees with roots t1 and t2 are equal.
        Works by recursively checking whether their left and right
        children are equal.
    """
    global EQUAL

    if not t1 and not t2:
        EQUAL = True
        return EQUAL

    if not t1 or not t2:
        EQUAL = False
        return EQUAL

    if t1 and t2:
        if t1.left == t2.left and t1.right == t2.right:
            check_equal_trees(t1.left, t2.left)
            check_equal_trees(t1.right, t2.right)

    return EQUAL


def check_subtree(t1, t2):
    """
    Applies both above algorithms to check for Tree t2, in Tree t2.
    """
    root = find_x(t1, t2.data)
    if root:
        if check_equal_trees(root, t2):
            return True
        return False
    else:
        return False


if __name__ == "__main__":
    a = TreeNode(4)
    b = TreeNode(2)
    c = TreeNode(6)
    d = TreeNode(1)
    e = TreeNode(3)
    f = TreeNode(5)
    g = TreeNode(7)

    # construct T1
    a.left = b
    a.right = c

    b.left = d
    b.right = e

    c.left = f
    c.right = g

    print(check_subtree(a, g))