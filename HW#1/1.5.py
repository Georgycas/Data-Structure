class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def calculateLinkedListAverage(head_node):
    count = 0
    total = 0
    current = head_node
    while current:
        count += 1
        total += current.val
        current = current.next
    if count == 0:
        return 0
    else:
        return total / count


# Create a linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

curr = head
while curr:
    print(curr.val, end="->")
    curr = curr.next
print("")


# Calculate the average value of the linked list
avg = calculateLinkedListAverage(head)

# Print the average value
print(avg)
