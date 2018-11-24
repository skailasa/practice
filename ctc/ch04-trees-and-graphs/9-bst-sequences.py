"""
A BST is created by traversing through an array left to right and
    inserting each element. Given a BST with distinct elements, print
    all possible arrays that could have led to this tree.

Strategy:
    - root node always first, a different first element would make a
    different BST
    - need to 'weave' together possible arrays and prepend root node
    to find final sequence.
    - Have to make sure that relative order is maintained, can do this
    recursively
    - Have to then implement a second recursive function to do this on
    each branch of a given root.
"""
import copy


class TreeNode:
    """Simple node class for binary tree"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


def weave(first, second, results, prefix):

    # if one list is empty add remainder to cloned prefix, and store
    if not first or not second:
        result = copy.deepcopy(prefix)
        result.extend(first)
        result.extend(second)
        results.append(result)
        return

    # recurse with head of first added to the prefix. Removing the head
    # will damage first, so we'll need to replace it
    head_first = first[0]
    prefix.append(head_first)
    first = first[1:]
    weave(first, second, results, prefix)
    first = [head_first] + first
    prefix.pop()

    head_second = second[0]
    prefix.append(head_second)
    second = second[1:]
    weave(first, second, results, prefix)
    prefix.pop()


def all_sequences(node):
    result = []

    if not node:
        return result

    prefix = list()
    prefix.append(node.data)

    result.append(prefix)

    left_sequences = all_sequences(node.left)
    right_sequences = all_sequences(node.right)

    # weave together each list from left and right sides
    for left in left_sequences:
        for right in right_sequences:
            weaved = []
            weave(left, right, weaved, prefix)
            result.extend(weaved)

    return result


if __name__ == "__main__":
    a = TreeNode(4)
    b = TreeNode(2)
    c = TreeNode(6)
    #d = TreeNode(1)
    #e = TreeNode(3)
    #f = TreeNode(5)
    #g = TreeNode(7)

    # construct simple BST
    a.left = b
    a.right = c

    #b.left = d
    #b.right = e

    #c.left = f
    #c.right = g

    print(all_sequences(a))

