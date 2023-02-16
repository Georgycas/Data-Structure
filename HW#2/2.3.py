class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def monkey_king_election(n, m):
    # Create the circular linked list
    head = Node(0)
    curr = head
    for i in range(1, n):
        curr.next = Node(i)
        curr = curr.next
    curr.next = head

    # Traverse the list, skipping every mth node
    prev = None
    curr = head
    for i in range(n-1):
        for j in range(m):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        curr = prev.next

    # Return the remaining node
    return curr.data

# Get input from user
n = int(input("Enter total number of monkeys in a group: "))
m = int(input("Enter m value: "))

# Find the monkey king
king = monkey_king_election(n, m)

# Print the result
print("The king will be", king)
