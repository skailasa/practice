"""
Write an algorithm to find the 'next' node. i.e. in-order successor of
a given node in a BST.
You may assume that each node has  a link to it's parent.

Strategy:
    - Try going to right child, and then the right child's furthest
    possible left successor.
    - Otherwise, go to parent, if parent > than current node return
    parent
        - Otherwise return grandparent
        - Otherwise return None, you're on the last (biggest) node.
"""


class TreeNode:
    """Simple node class for binary tree"""
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.parent = None
        self.visited = False

    def visit(self):
        self.visited = True


def find_left_grandchild(node):
    """
    Find the furthest left grandchild of a given node
    Complexity:
        O(logN) as at most we'll have to recurse to bottom of tree
    """
    if node.left:
        return find_left_grandchild(node.left)
    return node


def successor(node):
    """
    Find the succesor using the strategy above
    Complexity: Bottleneck is the recursive call to find left grandchild
        Otherwise fixed cost comparison of O(1) which occurs when we don't
        have a right descendent. Happens ~ 2^i/N times where i is the
        depth of the BST. i scales as log(N), can expect it to happen
        1/N log(N) times for large N, log(N) << N, so can expect on average
        to do better than log(N) for whole algorithm, amortized runtime
        probably O(1)
    """
    if node.right:
        successor = find_left_grandchild(node.right)

    else:
        if node.parent:
            if node.parent.name > node.name:
                successor = node.parent
            elif node.parent.name < node.name:
                if node.parent.parent.name > node.name:
                    successor = node.parent.parent
                else:
                    successor = TreeNode(None)

    return successor

if __name__ == "__main__":
    n2 = TreeNode(2)
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    # construct simple BST
    n2.left = n1
    n2.right = n3

    n1.parent = n2
    n3.parent = n2

    n3.right = n4
    n4.right = n5

    n4.parent = n3
    n5.parent = n4

    print(successor(n1).name)
