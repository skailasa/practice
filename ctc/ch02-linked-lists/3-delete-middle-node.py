"""
Delete the middle node in a Linked List, when only given access to this
node object.

Use my custom Python Linked list implementation from my blog
(https://skailasa.github.io/2018/12/23/datastructures.html)
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

    def search(self, data):
        """Return the node that holds a given piece of data"""
        x = self.head

        while x.data != data:
            x = x.next

        return x

    def remove(self, data):
        """Splice out a given node"""

        x = self.search(data)

        x.prev.next = x.next
        x.next.prev = x.prev

        if x.data == self.head.data:
            self.head = x.next