"""
Write a function to rotate a matrix in place
"""


def rotate(M):
    n_layers = int(len(M)/2)
    n = len(M)

    for layer in range(n_layers):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = M[first][i]

            # left -> top
            M[first][i] = M[last-offset][first]

            # bottom -> left
            M[last-offset][first] = M[last][last-offset]

            # right -> bottom
            M[last][last-offset] = M[i][last]

            # top -> right
            M[i][last] = top


def main():

    M = [
        ['a', 'c'],
        ['b', 'd'],
    ]

    rotate(M)

    print(M)


if __name__ == "__main__":
    main()