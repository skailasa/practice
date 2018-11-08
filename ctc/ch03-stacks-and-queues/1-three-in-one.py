"""
Use a single array to implement three stacks
"""


class StackArray:
    """
    3 stacks built out of a single array, absolutely filthy implementation.
    """
    def __init__(self, max_len):
        if max_len < 3:
            raise TypeError("Must have an underlying array with at least 3 spaces")

        self._max_len = max_len
        self._len_1, self._len_2, self._len_3 = self.stack_length(max_len)
        self._stack = [None] * max_len

    def __len__(self):
        return self._max_len

    def __repr__(self):
        return str(self._stack)

    @staticmethod
    def stack_length(max_len):
        remainder = max_len % 3
        div = max_len // 3
        if remainder:
            stack_1, stack_2 = div, div
            stack_3 = div + remainder
        else:
            stack_1, stack_2, stack_3 = div, div, div

        return stack_1, stack_2, stack_3

    @staticmethod
    def number_of_spaces(stack):
        c = 0
        for i in stack:
            if i is None:
                c += 1
        return c

    @staticmethod
    def next_free_index(stack):
        temp = [i for i, x in enumerate(stack) if x is None]
        if temp:
            return temp[-1]
        else:
            return len(stack) - 1

    def pop(self, stack):
        if stack == 0:
            stack1 = self._stack[:self._len_1]
            idx = self.next_free_index(stack1) + 1
            stack1[idx] = None
            self._stack[:self._len_1] = stack1
        elif stack == 1:
            stack2 = self._stack[self._len_1:self._len_1+self._len_2]
            idx = self.next_free_index(stack2) + 1
            stack2[idx] = None
            self._stack[self._len_1:self._len_1 + self._len_2] = stack2
        elif stack == 2:
            stack3 = self._stack[self._len_1 + self._len_2:]
            idx = self.next_free_index(stack3) + 1
            stack3[idx] = None
            self._stack[self._len_1 + self._len_2:] = stack3

    def push(self, item, stack):
        if stack == 0:
            stack1 = self._stack[:self._len_1]
            if self.number_of_spaces(stack1) == 0:
                raise ValueError("Stack Full")
            else:
                free_idx = self.next_free_index(stack1)
                stack1[free_idx] = item
            self._stack[:self._len_1] = stack1

        if stack == 1:
            stack2 = self._stack[self._len_1:self._len_1+self._len_2]
            if self.number_of_spaces(stack2) == 0:
                raise ValueError("Stack Full")
            else:
                free_idx = self.next_free_index(stack2)
                stack2[free_idx] = item
            self._stack[self._len_1:self._len_1+self._len_2] = stack2

        if stack == 2:
            stack3 = self._stack[self._len_2+self._len_1:]
            if self.number_of_spaces(stack3) == 0:
                raise ValueError("Stack Full")
            else:
                free_idx = self.next_free_index(stack3)
                stack3[free_idx] = item
            self._stack[self._len_2 + self._len_1:] = stack3

    @property
    def empty(self):
        return not bool(self._stack)


if __name__ == "__main__":
    s = StackArray(3)
    print(s)
    s.push('a', 0)
    s.push('a', 0)
    # should raise ValueError for stack being full
    print(s)