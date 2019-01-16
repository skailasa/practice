"""
You have two numbers represented by a linked list where each node
contains a single digit. Digits stored in reverse order, so ones are stored
in first index/head of list.

Write a function that dds two numbers and returns the sum as a linked
list
"""


class Node:
    """
    Node to store data, and pointer to next node in linked list
        as well as a pointer to the previous node.
    """
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class LinkedList:
    """Implement using Nodes and Pointers"""
    def __init__(self):
        self.head = Node(None)

    def __repr__(self):
        """Some Python sugar to print a representation"""

        x = self.head
        ll = []
        while x.data is not None:
            ll.append(x.data)
            x = x.next

        return str(ll)

    def insert(self, data):
        """Insert an element at the head of the list"""
        node = Node(data)

        node.next = self.head
        self.head.prev = node

        self.head = node
        self.head.prev = Node(None)


def first_n_digits(num, n):
    return int(str(num)[:n])


def sum(ll1, ll2):

    curr_ll1 = ll1.head
    curr_ll2 = ll2.head
    carry = 0

    ll = LinkedList()

    while curr_ll1.data is not None and curr_ll1.data is not None:
        _sum = curr_ll1.data+curr_ll2.data + carry

        if _sum < 10:
            ll.insert(_sum)

        else:
            ll.insert(abs(_sum-10))
            carry = first_n_digits(_sum, 1)

        curr_ll1 = curr_ll1.next
        curr_ll2 = curr_ll2.next

    ll.insert(carry)

    print(ll)


if __name__ == "__main__":
    ll1 = LinkedList()
    ll2 = LinkedList()

    for i in ([9, 0]):  # 10
        ll1.insert(i)

    for i in ([1, 6]):  # 20
        ll2.insert(i)

    sum(ll1, ll2)

