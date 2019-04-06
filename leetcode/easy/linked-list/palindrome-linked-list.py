"""
Given a single linked list, determine if it's a palindrome.

Could you do it in O(n) time and O(1) space?
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def is_palindrome(head):
    """Reverse it, then iterate through all nodes"""
    forward = []

    while head is not None:
        forward.append(head.val)
        head = head.next

    # reverse linked list
    backward = list(reversed(forward))

    for i in range(len(forward)):
        if forward[i] != backward[i]:
            return False

    return True


if __name__ == "__main__":

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(2)
    n4 = Node(1)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    print(is_palindrome(n1))