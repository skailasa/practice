"""
How would you design a stack which in addition to push and pop has
a 'min' function which returns the minimum element.
All operations should be O(1).
"""


class Node:
    """Stack Node"""
    def __init__(self, val):
        self.val = val
        self._min = val

    def __repr__(self):
        return str((self.val, self.min))

    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, val):
        self._min = val


class Stack:
    """
    Stack with O(1) 'min' operation
    """
    def __init__(self):
        self._stack = [Node(99999)]

    def __repr__(self):
        return str(self._stack[1:])

    @property
    def _top_node(self):
        return self._stack[-1]

    def _find_min(self, val, top_node):
        if val < top_node.min:
            return val
        return top_node.min

    def pop(self):
        self._stack = self._stack[:-1]
        print('popped')

    def push(self, val):
        min = self._find_min(val, self._top_node)
        new_node = Node(val)
        new_node.min = min
        self._stack.append(new_node)

    def min(self):
        return self._stack[-1].min


if __name__ == "__main__":
    s = Stack()
    s.push(2)
    s.push(5)
    s.push(1)
    print(s.min())  # 1
    print(s)

