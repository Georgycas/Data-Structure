class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLinkedList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# Create a linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Reverse the linked list
head = reverseLinkedList(head)

# Print the reversed linked list
curr = head
while curr:
    print(curr.val, end="->")
    curr = curr.next
