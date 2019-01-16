"""
Check if the edit distance of two strings is one or zero
"""

from collections import Counter


def check_large_edit_distance(s1, s2):
    if len(set(s1).symmetric_difference(set(s2))) > 1:
        return True

    return False


if __name__ == "__main__":
    print(check_large_edit_distance('sri', 'srisfsdf'))