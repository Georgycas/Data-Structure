class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_loopLL(head: ListNode) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Test Case 1
# create a linked list with a loop
node4 = ListNode(4)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
node4.next = node2
head = node1

# expected output: True
print(is_loopLL(head))

# Test Case 2
# create a linked list without a loop
node4 = ListNode(4)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head = node1

# expected output: False
print(is_loopLL(head))
