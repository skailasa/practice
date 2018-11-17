"""
Implement a function to check whether a binary tree is a binary search
    tree.

Strategy:
    - can recurse down left
        - just need to find max value, check if this is greater than
        rot can stop recursion, and BST is invalid.
"""


class TreeNode:
    """Simple node class for binary tree"""
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.visited = False

    def visit(self):
        self.visited = True


def max_node(node, root_val):
    """Run on node left of root"""

    max_val = root_val

    if node:
        # check against max value
        if node.name > max_val:
            max_val = node.name
            return max_val
        else:
            return max(max_node(node.left, root_val), max_node(node.right, root_val))

    return max_val


def validate_bst(root):
    root_val = root.name

    max_left_val = max_node(root.left, root_val)

    if max_left_val > root_val:
        print("NOT a valid BST")
        return
    print("Valid BST")
    return


if __name__ == "__main__":
    n2 = TreeNode(2)
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    # construct simple BST
    n2.left = n1
    n2.right = n3
    n3.right = n4
    n4.right = n5

    #print(n1.height)

    validate_bst(n2)

