"""
Implementation of a hash table using linked lists
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
        return str(self._list)

    def __len__(self):
        return len(self._list)

    @property
    def _list(self):
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


def small_hash(value):
    return hash(value) % 10


class HashTable:
    """Simple Hashtable implementaiton using linked lists"""

    def __init__(self):
        # buffer space
        self._table = [None]*int(1e6)
        self._values = []

    def __repr__(self):
        items = []
        for v in self._values:
            items.append((v, self._table[small_hash(v)]))

        return str(items)

    def __setitem__(self, value, item):
        key = small_hash(value)
        ll = LinkedList()
        ll.add(item)

        if value not in self._values:
            self._values.append(value)

        self._table[key] = ll

    def __getitem__(self, value):
        key = small_hash(value)
        return self._table[key]


if __name__ == "__main__":

    h = HashTable()
    h['a'] = 'b'
    h['b'] = 'c'
    print(h['a'])  # 'b'
    print(h['b'])  # 'c'

