"""
Write an algorithm to print all ways of arranging eight queens on an 8x8
    chess board such that none of them share the same row, column or
    diagonal.
"""


def board(N):
    return [[None for i in range(N)] for j in range(N)]


def is_safe(N, board, row, col):
    """
    Only need to check that queens already placed do not conflict with
        current queen being considered for position (row, col).
    """
    for i in range(col):
        if board[row][i]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def n_queens(N, board, col):

    # base case, if we have placed all queens, then return True
    if col >= N:
        return True

    for i in range(N):

        if is_safe(N, board, i, col):
            # for each possible column position, try to place a queen
            board[i][col] = True

            # recurse up call stack, if we've reached the base case then
            # we've found a winning position for this queen.
            if n_queens(N, board, col + 1):
                return True

            # otherwise set this position back to None, and try the next
            # position.
            board[i][col] = None

    # if no combinations are possible, return False
    return False


if __name__ == "__main__":
    N = 4
    b = board(N)
    n_queens(N, b, 0)

    print(b)