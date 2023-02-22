class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def rotate_DLL(head, n):
    if not head or not head.next:
        return head

    # Get the length of the linked list
    curr = head
    length = 0
    while curr:
        length += 1
        curr = curr.next

    # Handle edge cases
    n = n % length
    if n == 0:
        return head

    # Find the new tail and head nodes after rotation
    tail = head
    for i in range(length - n - 1):
        tail = tail.next
    new_head = tail.next
    new_head.prev = None
    tail.next = None

    # Connect the new head and tail nodes to the old head and tail nodes
    curr = new_head
    while curr.next:
        curr = curr.next
    curr.next = head
    head.prev = curr
    return new_head


# Create a doubly linked list
head = Node('c')
head.prev = None
head.next = Node('i')
head.next.prev = head
head.next.next = Node('v')
head.next.next.prev = head.next
head.next.next.next = Node('i')
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node('c')
head.next.next.next.next.prev = head.next.next.next
head.next.next.next.next.next = None

# Rotate the doubly linked list
new_head = rotate_DLL(head, 3)

# Traverse the rotated doubly linked list and print the values
curr = new_head
while curr:
    print(curr.val, end=" ")
    curr = curr.next
