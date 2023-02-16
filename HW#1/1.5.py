class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def calculateLinkedListAverage(head):
    count = 0
    total = 0
    curr = head
    while curr:
        count += 1
        total += curr.val
        curr = curr.next
    if count == 0:
        return 0
    else:
        return total / count

# Create a linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Calculate the average value of the linked list
avg = calculateLinkedListAverage(head)

# Print the average value
print(avg)
