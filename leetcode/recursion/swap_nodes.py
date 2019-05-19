class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None


def swapPairs(head):
	if head is None or head.next is None:
		return head

	head.next.next = swapPairs(head.next.next)

	newCur = head.next;
	head.next = newCur.next;
	newCur.next = head;
        
	return newCur



if __name__ == "__main__":
	l1 = ListNode(1)
	l2 = ListNode(2)
	l3 = ListNode(3)
	l4 = ListNode(4)
	l5 = ListNode(5)


	l1.next = l2
	l2.next = l3
	l3.next = l4
	l4.next = l5

	swapPairs(l1)

	print(l1.next.val)
	print(l2.next.val)
