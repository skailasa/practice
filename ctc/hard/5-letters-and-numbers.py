"""
Given an array filled with letters and numbers, find the longest
    subarray with an equal number of letters and numbers.

Strategy:
    - consider [a a 1 1 a a a 1 1 1]
    - the longeest subarray that satisfies the problem is [a a a 1 1 1]
    - just need to variables that count the number of letters passed and
        numbers passed, and another that calculates the difference
        between these two variables. Whenever the distance measure is
        repeated it signals a subarray with an equal number of letters
        and numbers
        - just need to find the longest one of these.
"""
from collections import defaultdict


def max_subarray(l):
    nums_passed = 0
    letters_passed = 0
    difference = [0]
    idxs = defaultdict(list)
    max_diff = 0

    for ch in l:
        if isinstance(ch, int):
            nums_passed += 1
        elif isinstance(ch, str):
            letters_passed += 1

        difference.append(abs(nums_passed-letters_passed))

    for idx, d in enumerate(difference):
        idxs[d].append(idx)

    for k, v in idxs.items():
        if len(v) > 1:
            if len(v) > max_diff:
                max_diff = len(v)
                res = l[v[0]: v[-1]]

    print(res)


if __name__ == "__main__":
    l = ['a', 'a', 'a', 1, 'a', 1]  # answer: ['a', 1, 'a', 1]

    max_subarray(l)