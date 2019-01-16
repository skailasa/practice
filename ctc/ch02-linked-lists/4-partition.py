"""
Partition a linked list around a pivot value such that all nodes to its
left are smaller than the pivot, and all nodes to the right are larger
than or equal in value.
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

    def search(self, data):
        """Return the node that holds a given piece of data"""
        x = self.head

        while x.data != data:
            x = x.next

        return x

    def partition(self, pivot):
        p = Node(pivot)
        pivot_left_pointer = p
        pivot_right_pointer = p

        x = self.head
        ll = []
        while x.data is not None:
            if x != p:
                ll.append(x)
            x = x.next

        for n in ll:
            if n.data < p.data:
                n.next = pivot_left_pointer
                pivot_left_pointer.prev = n

                pivot_left_pointer = n
                pivot_left_pointer.prev = Node(None)

            else:
                n.prev = pivot_right_pointer
                pivot_right_pointer.next = n

                pivot_right_pointer = n
                pivot_right_pointer.next = Node(None)

        for n in ll:
            print(n.prev.data, n.data, n.next.data)


if __name__ == "__main__":

    ll = LinkedList()

    for i in [1, 2, 4,3, 5]:
        ll.insert(i)

    #print(ll)

    ll.partition(3)

