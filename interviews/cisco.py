"""
Write some code to draw a table, where the padding of each cell is equal
to the size of the largest number in the table, and the number of columns
is specified by a parameter K. The other input is an array A of numbers
that are to be placed in the table.

Example Usage:
>>> A = [1, 2, 3, 400]
>>> K = 2
>>> t = Table(A, K)
>>> t.draw_table()
+---+---+
|  1|  2|
+---+---+
|  3|400|
+---+---+
"""


class Cell:
    """Encapsulate the properties of each cell"""
    def __init__(self, val, max_size=None):
        self.val = str(val)
        if not max_size:
            self.max_size = len(str(val))
            self.padded_value= str(val)

        else:
            self.max_size = max_size
            self.padded_value = " "*(max_size-len(self.val))+self.val

    @property
    def value(self):
        return self.padded_value


class Table:
    """Compose a Table object from many Cells"""
    def __init__(self, A, K):
        self.A = A
        self.K = K
        self.max_cell_size = len(str(max(A)))
        self.n_chunks = min([K, len(A)])
        self.top = ("+" + "-" * self.max_cell_size) * self.n_chunks + "+"
        self.side = "|"

    @staticmethod
    def _chunks(l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def draw_row(self, values):
        row = self.top + "\n"
        for val in values:
            row += self.side + Cell(val,
                                    max_size=self.max_cell_size).value

        row += "|"
        return row

    def draw_table(self):
        _len_last_chunk = 0
        for chunk in self._chunks(self.A, self.K):
            _len_last_chunk = len(chunk)
            print(self.draw_row(chunk))

        print(("+" + "-" * self.max_cell_size) * _len_last_chunk + "+")


if __name__ == "__main__":
    t = Table(A=[1, 2, 3, 400], K=2)
    t.draw_table()