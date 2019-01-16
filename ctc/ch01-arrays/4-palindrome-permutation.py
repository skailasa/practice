"""
Write a function to check if a string is a permutation of a palindrome.
The palindrome does not have to be real words
"""

from collections import Counter


def permutation_of_palindrome(s):
    """
    Can also implement with dicts, but this is more pythonic (and faster!)
    """
    c = Counter(s)

    for v in c.values():
        if v % 2:
            return False

    return True


if __name__ == "__main__":
    print(permutation_of_palindrome('caca'))