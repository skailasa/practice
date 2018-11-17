"""
Implement a function to check whether a binary tree is balanced. In this
    question, a balanced tree is defined to be a tree such that the
    heights of any two subtrees of any node never differ by more than 1.
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

    @staticmethod
    def _height(node):
        if not node:
            return -1
        else:
            return max(
                TreeNode._height(node.left), TreeNode._height(node.right)
            ) + 1

    @property
    def height(self):
        return TreeNode._height(self)


def check_balanced(root):
    lheight = root.left.height
    rheight = root.right.height

    if abs(lheight-rheight) > 1:
        print("unbalanced")
        return
    print("balanced")
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

    check_balanced(n2)

