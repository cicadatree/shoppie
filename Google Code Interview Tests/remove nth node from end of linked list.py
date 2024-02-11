class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    first = dummy
    second = dummy

    for _ in range(n + 1):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next
    return dummy.next

# Example usage
# Assuming you have a linked list created and `head` is the head of that list
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# result = removeNthFromEnd(head, 2)

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = removeNthFromEnd(node1, 2)
print(list(head))
