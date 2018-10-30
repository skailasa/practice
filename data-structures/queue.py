"""
Implements a FIFO ordering
e.g. A queue in real life

Supports the following operations:
- add(item),  added to the end of a queue
- remove(item), remove the first item in queue
= peek(), return the top of the queue
- isEmpty(), return true iff queue empty

Can be implemented with linked lists, they are essentially the same
thing, as long as items are added/removed from opposite sides.

Often used in breadth-first search or implementing a cache
"""

class Node:
    """Node object, storing data and pointer"""
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    """Implementation of queue using Linked List"""

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        """Add item to queue"""
        new_item = Node(item)

        # check if queue is empty
        if self.head == self.tail == None:
            self.head = self.tail = new_item
            return None
        
        else:
            self.head = new_item
            self.head.next = new_item
        
    def remove(self):
        """Remove item from queue"""
        if self.isEmpty():
            return None
        else:
            temp = self.head
            self.head = temp.next

            if self.head == None:
                self.tail = None
        
    def peek(self):
        "Peek on top of queue"""
        if self.head:
            return self.head.data
        return "Empty Queue"
        
    def isEmpty(self):
        """Return true iff queue is empty"""
        return not bool(self.head)


if __name__ == "__main__":
        q = Queue()
        q.add("sri")
        print(q.peek())
        q.remove()
        print(q.peek())
