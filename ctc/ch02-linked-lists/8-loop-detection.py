"""
Detect if a singly linked list is circular
"""


class Node:
    """
    Node to store data, and pointer to next node in linked list
        as well as a pointer to the previous node.
    """
    def __init__(self, data):
        self.next = None
        self.data = data


def loop_detection(head):

    _node_dict = {}
    while head.next is not None:

        if head.next not in _node_dict.values():
            _node_dict[head.data] = head

        else:
            return True
        head = head.next


if __name__ == "__main__":

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    n1.next = n2
    n2.next = n3
    n3.next = n1

    print(loop_detection(n1))
