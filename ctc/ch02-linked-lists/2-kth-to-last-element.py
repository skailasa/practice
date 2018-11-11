"""
Find the kth to last element of a singly linked list
"""


class Node:
    """
    Simple node object.
        - attr storing one piece of 'data'
        - attr storing pointer to next node
    """

    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self): return self._data

    @data.setter
    def data(self, new): self._data = new

    @property
    def next(self): return self._next

    @next.setter
    def next(self, new): self._next = new


class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self._head = None

    def __repr__(self):
        return str(self.list)

    def __len__(self):
        return len(self.list)

    @property
    def list(self):
        end = False
        _list = []
        temp_head = self._head
        while not end:
            if temp_head is None:
                end = True
            else:
                _list.append(temp_head.data)
                temp_head = temp_head.next
        return _list

    @property
    def empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.next = self._head
        self._head = temp

    def find_kth_last(self, k):
        return self.list[-k]


if __name__ == "__main__":
    l = LinkedList()
    l.add('i')
    l.add('r')
    l.add('s')

    print(l)
    print(l.find_kth_last(3))