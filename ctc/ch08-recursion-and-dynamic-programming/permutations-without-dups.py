"""
Write a method to compute all permutations of a string of unique
    characters.
"""


PERMUTATIONS = []


def permute(s, length):

    if len(s) == 1:
        return s

    else:
        for idx, ch in enumerate(s):
            pref = ch
            remainder = s[:idx] + s[idx+1:]
            res = pref + permute(remainder, length)

            if len(res) == length:
                PERMUTATIONS.append(res)

    return res


if __name__ == "__main__":
    s = 'abc'

    length = len(s)

    permute(s, length)

    print(PERMUTATIONS)