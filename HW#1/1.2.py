class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteNodeWithValue(head, value):
    # Handle the case where the head node has the target value.
    while head and head.val == value:
        head = head.next

    curr = head
    while curr and curr.next:
        if curr.next.val == value:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head


def deleteDuplicateNodes(head):
    # Handle empty or singleton linked list case.
    if not head or not head.next:
        return head

    # Create a dictionary to keep track of node values.
    values = {}
    curr = head
    while curr:
        if curr.val not in values:
            values[curr.val] = 1
        else:
            values[curr.val] += 1
        curr = curr.next

    # Delete nodes with duplicate values.
    for value, count in values.items():
        if count > 1:
            head = deleteNodeWithValue(head, value)

    return head

# Create linked list with duplicates
head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(3)
head.next.next.next.next = Node(2)

# Delete nodes with duplicated values
head = deleteDuplicateNodes(head)

# Print the new linked list
curr = head
while curr:
    print(curr.val, end="->")
    curr = curr.next
