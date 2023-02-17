class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def deleteDuplicateNodes(head_node):
    # Handle empty or singleton linked list case.
    if not head_node or not head_node.next:
        return head_node

    # Create a dictionary to keep track of node values.
    values = {}
    current = head_node
    while current:
        if current.val not in values:
            values[current.val] = 1
        else:
            values[current.val] += 1
        current = current.next

    # Create a new linked list with unique nodes.
    new_head = Node()
    current = new_head
    old_curr = head_node
    while old_curr:
        if values[old_curr.val] == 1:
            current.next = Node(old_curr.val)
            current = current.next
        old_curr = old_curr.next

    return new_head.next


# Create linked list with duplicates
head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(3)
head.next.next.next.next = Node(2)

curr = head
while curr:
    print(curr.val, end="->")
    curr = curr.next
print("")

# Delete nodes with duplicated values
head = deleteDuplicateNodes(head)

# Print the new linked list
curr = head
while curr:
    print(curr.val, end="->")
    curr = curr.next
