"""
Implement an algorithm to print all valid (e.g. properly open and closed)
    combinations of n pairs of parenthesis.
"""


COMBINATIONS = []


def paren(n):

    if n == 1:
        res = ['()']
        COMBINATIONS.append(res)
        return res

    else:
        r1 = ['('+r+')' for r in paren(n-1)]
        r2 = ['()'+r for r in paren(n-1)]
        res = r1 + r2

        COMBINATIONS.append(res)

    return res


if __name__ == "__main__":

    paren(3)

    print(COMBINATIONS[-1])