"""
Using logic of hare/tortoise algorithm to detect cycle
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def find_cycle(head):

    hare = head
    tortoise = head

    detected = False

    while not detected:

        if hare.next and tortoise.next:
            if hare.next.next:

                hare = hare.next.next
                tortoise = tortoise.next
                # check if they've collided:
                if hare == tortoise:
                    return True
            else:
                return False
        else:
            return False



if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    sentinel = Node(1000)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n1

    print(find_cycle(n1))