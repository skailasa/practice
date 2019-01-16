"""
Given two singly linked lists, determine if the two lists intersect, returning
the intersecting node. Note that the intersection is based on reference and
NOT value.


Two intersecting linked lists will share a common final node:

a -> b -> c -> d
          ^
          |
e -> f -> -

Therefore, we must iterate through all of a one of the linked lists,
checking for the intersection.

This has very poor complexity,
it would probably be better to hash all the nodes from each linked list
and take an intersection of keys
"""


class Node:
    """
    Node to store data, and pointer to next node in linked list
        as well as a pointer to the previous node.
    """
    def __init__(self, data):
        self.next = None
        self.data = data


def find_final_node(ll_head):

    while ll_head is not None:
        if ll_head.next is None:
            return ll_head
        ll_head = ll_head.next


def check_intersection(ll1_head, ll2_head):

    ll1_final = find_final_node(ll1_head)
    ll2_final = find_final_node(ll2_head)

    if ll1_final is not ll2_final:
        return False

    return True


def find_intersecting_node(ll1_head, ll2_head):

    if ll1_head is ll2_head:
        return ll1_head.data

    elif ll1_head.next:
        return find_intersecting_node(ll1_head.next, ll2_head)

    return None


def main():
    """
    n1 -> n2 -> n4 -> n5
                ^
                |
                n3
    """

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    n1.next = n2  # head of linked list 1, ll1
    n2.next = n4

    n3.next = n4  # head of linked list 2, ll2

    n4.next = n5

    ll2 = [n3, n4, n5]  # iterate over all nodes in ll2

    for n in ll2:
        if find_intersecting_node(n1, n):
            print(n.data)
            break


if __name__ == "__main__":
    main()