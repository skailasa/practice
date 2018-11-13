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
    """Simple Hashtable implementation using linked lists"""

    def __init__(self):
        # buffer space
        self._table = [None for i in range(100)]
        self._values = []

    def __repr__(self):

        l = []
        for v in self._values:
            l.append((v, self._table[small_hash(v)]))

        return str(l)

    def __setitem__(self, value, item):

        key = small_hash(value)

        if value not in self._values:
            self._values.append(value)

        if not self._table[key]:
            self._table[key] = LinkedList()

        self._table[key].add(item)

    def __getitem__(self, value):
        key = small_hash(value)

        return self._table[key]


class Set(HashTable):
    """HashTable where the key and value are the same"""
    def __init__(self, iterable):
        super().__init__()
        self._set = HashTable()
        for item in iterable:
            self._set[item] = item

    def __repr__(self):
        return str(self._set)


class Dict(HashTable):
    """HashTable where a key maps to a value"""
    def __init__(self):
        super().__init__()


if __name__ == "__main__":

    h = HashTable()
    h['a'] = 'b'
    h['a'] = 'c'
    h['b'] = 'd'

    print(h)

