"""
Remove duplicates from an unsorted linked list
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
        end = False
        _repr = []
        temp_head = self._head
        while not end:
            if temp_head is None:
                end = True
            else:
                _repr.append(temp_head.data)
                temp_head = temp_head.next
        return str(_repr)

    @property
    def empty(self):
        return self._head == None

    def add(self, item):
        temp = Node(item)
        temp.next = self._head
        self._head = temp

    def remove_duplicates(self):
        """
        Method to remove duplicates
        """
        buffer = []
        hashmap = set()
        current = self._head
        end = False

        while not end:
            if set(current.data).intersection(hashmap):
                pass
            else:
                hashmap.add(current.data)
                buffer.append(current.data)

            current = current.next
            if current is None:
                end = True

        l = LinkedList()
        [l.add(d) for d in buffer]
        return l

if __name__ == "__main__":
    l = LinkedList()
    l.add('a')
    l.add('b')
    l.add('a')
    l.add('a')

    l = l.remove_duplicates()
    print(l)