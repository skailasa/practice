"""
Array like data structure 'Listy', which lacks a size method.
It does have an elementAt(i) method that returns the element
at index i, in O(1) time. If i is beyond the bounds of the
datastructure it returns -1, hence can only contain positive
integers.

Given that a Listy object contains sorted positive integers, find
the index at which an element x occurs. If x occurs multiple times
you may return any index.

-- Can't use binary search off the bat as we don't know how long
the list is.

- Have to find the bounds of the list and then perform binary search
"""

