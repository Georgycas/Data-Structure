class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverseLinkedList(head_node):
    prev = None
    current = head_node
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


# Create a linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

curr = head
while curr:
    print(curr.val, end="->")
    curr = curr.next
print("")

# Reverse the linked list
head = reverseLinkedList(head)

# Print the reversed linked list
curr = head
while curr:
    print(curr.val, end="->")
    curr = curr.next
