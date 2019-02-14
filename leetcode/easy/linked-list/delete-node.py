"""
Delete the nth from last node in a single linked list.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def delete_node(head, n):

    if head.next is None:
        return None

    _head = head
    found = False
    curr = head
    while not found:
        temp = curr
        for i in range(n):
            temp = temp.next
            if temp.val == 1000 and i == n-1:
                found = True

        if not found:
            curr = curr.next

    # find new head
    if curr == _head:
        _head = curr.next

    curr.val = curr.next.val
    curr.next = curr.next.next

    return _head


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    sentinel = Node(1000)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = sentinel

    print(delete_node(n1, 1).next.next.next.val)
