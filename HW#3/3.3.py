class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def delete_prime_CLL(header):
    """Delete all prime number nodes from a circular linked list."""
    if not header:
        return None

    # Find the tail node of the circular linked list
    tail = header
    while tail.next != header:
        tail = tail.next

    # Traverse the circular linked list and remove prime number nodes
    curr = header
    prev = tail
    while curr.next != header:
        if is_prime(curr.val):
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next

    # Check if the head node is prime
    if is_prime(header.val):
        # Move the head node to the next non-prime node
        header = header.next
        tail.next = header

    return header


# Create a circular linked list with some prime and non-prime numbers
head = Node(13)
head.next = Node(12)
head.next.next = Node(15)
head.next.next.next = Node(14)
head.next.next.next.next = head

# Delete prime number nodes from the circular linked list
head = delete_prime_CLL(head)

# Print the updated circular linked list
current = head
while current.next != head:
    print(current.val, end=" -> ")
    current = current.next
print(current.val)
