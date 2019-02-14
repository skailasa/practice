"""
Merge two sorted linked lists, this is very similar to the merge
operation in merge sort
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge(head_1, head_2):

    merged = False

    curr1 = head_1
    curr2 = head_2

    nodes = []
    while not merged:

        if curr2 is None or curr1 is None:
            break

        if curr1.val <= curr2.val:
            nodes.append(curr1)
            curr1 = curr1.next

        elif curr1.val > curr2.val:
            nodes.append(curr2)
            curr2 = curr2.next

    # merge remainder
    if curr2 is not None:
        while curr2 is not None:
            nodes.append(curr2)
            curr2 = curr2.next

    elif curr1 is not None:
        while curr1 is not None:
            nodes.append(curr1)
            curr1 = curr1.next

    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]

    nodes[-1].next = None

    return [n.val for n in nodes]


if __name__ == "__main__":

    # l1
    n1 = Node(4)
    n2 = Node(3)

    # l2
    n3 = Node(2)
    n4 = Node(4)

    n1.next = n2
    n3.next = n4


    print(merge(n1, n3))
