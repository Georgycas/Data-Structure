class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

    # Create a new linked list with unique nodes.
    new_head = Node()
    curr = new_head
    old_curr = head
    while old_curr:
        if values[old_curr.val] == 1:
            curr.next = Node(old_curr.val)
            curr = curr.next
        old_curr = old_curr.next

    return new_head.next


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
