"""Reverse a singly linked list, iteratively and recursively"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse(curr, prev=None):
    if curr is None:
        return

    else:
        reverse(curr.next, curr)
        curr.next = prev



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

    reverse(n1)

    print(n2.next.val)