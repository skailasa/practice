"""
Implementation of a linked list

Elements are not stored in contiguous blocks of memory. Instead
elements are linked via pointers.

Consists of nodes, where each node contains data as well as a reference
to the next node.

Insertion and deletion are cheaper compared to arrays as this is decided
at compile time for arrays.

Pros:
- Dynamic size
- Ease of insertion/deletion

Cons:
- No random access
- Extra mem required for pointer

"""

class Node:
    """Node object, storing data and pointer to next node """ 
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """LinkedList object, consists of nodes,
        beginning with a pointer to the first node"""
    def __init__(self):
        self.head = None
    
    def printList(self):
        """Print representation of a linked list"""
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


def main():
    """Create LL with 3 nodes """
    ll = LinkedList()
    ll.head = Node('s')
    second = Node('r')
    third = Node('i')

    ll.head.next = second
    second.next = third
    
    ll.printList()

if __name__ == "__main__":
    main()

