"""
Similar to singly-linked list but now contains a reference to previous node
as well as next node
"""
import copy


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):

        p = n = None

        if self.next:
            n = self.next.data
        if self.prev:
            p = self.prev.data

        return str(
            {
                "data": self.data,
                "previous": p,
                "next": n,
            }
        )


class LinkedList:
    """Doubly linked list"""

    def __init__(self):
        self._head = None
        self._tail = None

    def __repr__(self):
        return str([node for node in self._list])

    def __iter__(self):
        return iter(self._list)

    @property
    def _list(self):
        end = False
        _list = []
        temp_head = self._head
        while not end:
            if temp_head is None:
                end = True
            else:
                _list.append(temp_head)
                temp_head = temp_head.next
        return _list

    def push(self, item):
        """
        Have to update two pointers
        """
        temp = Node(item)

        if self._head is None:
            self._head = temp
            temp.prev = None
            temp.next = None
            self._tail = temp
        else:
            self._tail.next = temp
            temp.prev = self._tail
            self._tail = temp

    def pop(self):
        # pop current tail
        if self._tail:
            self._tail = self._tail.prev
            if self._tail:
                self._tail.next = None

            else:
                self._head = self._tail = None


if __name__ == "__main__":
    ll = LinkedList()
    ll.push('d')
    ll.push('a')
    ll.push('a')

    ll.pop()

    print(ll)
