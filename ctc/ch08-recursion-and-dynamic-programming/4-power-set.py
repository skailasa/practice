"""
Write a method to return all subsets of a set.

Strategy:
    - Base case, when there is just one item, return an empty set
    - Work through, noticing that
        n1 = n0 + [l.append(additional_element) for l in n0]
        where 'additional_element' is the element in n1 but not in n0.
"""


def subsets(s):
    if not s:
        # empty set
        return [[]]

    else:
        temp = subsets(s[1:])
        res = [l+[s[0]] for l in temp] + temp

    return res


if __name__ == "__main__":
    s = [1, 2, 3]
    print(subsets(s))

