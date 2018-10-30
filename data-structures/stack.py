"""
Stack: pretty much what it sounds like.
A stack of data, The order is LIFO/FILO
e.g. a stack of plates.

Supports the following operations:
- pop(), remove items from the top of a stack
- push(item), add to to top of a stack
- peek(), retur the top of a stack
- isEmpty(), return True if stack empty, else false

All of these are O(1) operations

Unlike arrays, doesn't allow constant time access to ith element.
This is because FILO/LIFO, however it does allow constant time add/remove
as we don't have to shift elements of stack around.

N.B A stack can also be implemented using a linked list
"""

class Stack:
    """Implementation using Lists"""
    def __init__(self):
        self._stack = []

    def pop(self):
        self._stack = self._stack[1:]

    def push(self, item):
        if self._stack:
            self._stack[0] = item
        else:
            self._stack.append(item)

    def peek(self):
        return self._stack[0]

    def isEmpty(self):
        return not bool(self._stack)


if __name__ == "__main__":
    stack = Stack()
     
    print("Check if Empty", stack.isEmpty())
    
    stack.push('sri')

    print("Peek into stack", stack.peek())

    print("Check if Empty", stack.isEmpty())
