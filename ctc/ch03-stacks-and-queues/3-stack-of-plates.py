"""
Implement a stack of stacks object that fills up stacks to their max
capacity, before creating a new top stack.

Strategy:
    - enforce a max size in the regular stack push and pop methods
"""


class Stack:
    def __init__(self):
        """Implement using a list"""
        self._stack = []
        self._size = 2

    def __repr__(self):
        return str(self._stack)

    @property
    def empty(self):
        """Check whether stack is empty"""
        return not bool(self._stack)

    @property
    def full(self):
        return len(self._stack) == self._size

    def push(self, v):
        """Add an item to top of stack"""
        if self.full:
            return False
        else:
            self._stack += [v]
            return True

    def pop(self):
        """Remove item from top of stack"""
        self._stack = self._stack[:-1]


class StackOfStacks:
    def __init__(self):
        self._stack = []

    def __repr__(self):
        return str(self._stack)

    def push(self, v):
        if not self._stack:
            self._stack.append(Stack())

        if not self._stack[-1].full:
            self._stack[-1].push(v)

        else:
            self._stack.append(Stack())
            self._stack[-1].push(v)

    def pop(self):
        if not self._stack:
            return []
        elif self._stack[-1].empty:
            self._stack = self._stack[:-1]

        self._stack[-1].pop()


def main():

    s = StackOfStacks()
    s.push(1)
    s.push(2)
    s.push(3)


    print(s)


if __name__ == "__main__":
    main()