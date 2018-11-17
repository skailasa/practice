"""
List of Depths:
    Given a binary tree, design an algorithm which creates a linked-list
    of all the nodes at each depth.

Strategy:
    Have to traverse the tree from a given node and create a linked-list
    - Can use in-order traversal, add nodes to linked list object.
"""


class ListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return str(self.list)

    @property
    def list(self):
        end = False
        _list = []
        temp_head = self.head
        while not end:
            if temp_head is None:
                end = True
            else:
                _list.append(temp_head.data)
                temp_head = temp_head.next
        return _list

    def add(self, item):
        temp = ListNode(item)
        temp.next = self.head
        self.head = temp


class TreeNode:
    """Simple node class for binary tree"""
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.visited = False

    def visit(self):
        self.visited = True



def create_linked_list(node, linked_list):
    """
    In order traversal, left branch visited before node, followed by
        right branch. Hence in order.
    """

    if node:
        create_linked_list(node.left, linked_list)
        linked_list.add(node.name)
        print(node.name)
        node.visit()
        create_linked_list(node.right, linked_list)

    return linked_list


if __name__ == "__main__":
    n2 = TreeNode(2)
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n4 = TreeNode(4)

    # construct simple BST
    n2.left = n1
    n2.right = n3
    n3.right = n4

    LL = LinkedList()
    LL = create_linked_list(n2, LL)

    print(LL)