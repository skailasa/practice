class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


def max_depth(root):
    if root is None:
        return 0

    else:
        ldepth = max_depth(root.left)
        rdepth = max_depth(root.right)

        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth + 1


if __name__ == "__main__":
    # define a simple tree

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(5)
    root.right.left = Node(4)

    root.right.right.right = Node(6)

    print(max_depth(root))