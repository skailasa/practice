"""
Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- getMin() -- Retrieve the minimum element in the stack.
"""


class MinStack:
    def __init__(self):
        self._stack = []

    def push(self, v):
        self._stack.append(v)

    def pop(self):
        self._stack = self._stack[:-1]

    def top(self):
        return self._stack[-1]

    def getMin(self):
        _min = self._stack[0]

        for s in self._stack:
            if s < _min:
                _min = s
            else:
                pass

        return _min
