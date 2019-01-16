"""
Write an algorithm st if an element in an MxN matrix is zero, so are its
entire row and column
"""


def zero_matrix(M):
    zero_cols = set()
    zero_rows = set()
    nvec = [0 for _ in range(len(M[0]))]

    for idx, vector in enumerate(M):
        for jdx, component in enumerate(vector):
            if component == 0:
                zero_cols.add(idx)
                zero_rows.add(jdx)

    for col in zero_cols:
        M[col] = nvec

    for col in zero_cols:
        for row in zero_rows:
            M[col][row] = 0


def main():
    M = [
        [0, 1, 2, 3, 22],
        [1, 3, 0, 123, 1]
    ]

    print(zero_matrix(M))


if __name__ == "__main__":
    main()

