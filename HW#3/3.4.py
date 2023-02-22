class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def split_CLL(head, N):
    # If the given head is None or the circular linked list has only one node, return None
    if not head or not head.next:
        return None

    # Traverse the circular linked list to find the node at index N-1
    curr = head
    for i in range(N - 1):
        curr = curr.next
        # If the index is out of bounds, return None
        if curr == head:
            return None

    # Create a new head for the second circular linked list
    new_head = curr.next

    # Set the next pointer of the node at index N-1 to the head of the circular linked list
    curr.next = head

    # Traverse the second circular linked list to find the tail node
    tail = new_head
    while tail.next != head:
        tail = tail.next

    # Set the next pointer of the tail node to the new head of the second circular linked list
    tail.next = new_head

    return head, new_head


# Create the original circular linked list
head = Node(2)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(5)
head.next.next.next.next = Node(6)
head.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next = head

# Split the circular linked list at index 3
new_head1, new_head2 = split_CLL(head, 3)

# Print the first circular linked list
current = new_head1
while current.next != new_head1:
    print(current.val, end=" -> ")
    current = current.next
print(current.val)

# Print the second circular linked list
current = new_head2
while current.next != new_head2:
    print(current.val, end=" -> ")
    current = current.next
print(current.val)
