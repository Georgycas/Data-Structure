class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteNodeWithValue(head_node, value):
    # Handle the case where the head node has the target value.
    while head_node and head_node.data == value:
        head_node = head_node.next

    current = head_node
    while current and current.next:
        if current.next.data == value:
            current.next = current.next.next
        else:
            current = current.next

    return head_node


def deleteDuplicateNodes(head_node):
    # Handle empty or singleton linked list case.
    if not head_node or not head_node.next:
        return head_node

    # Create a dictionary to keep track of node values.
    values = {}
    current = head_node
    while current:
        if current.data not in values:
            values[current.data] = 1
        else:
            values[current.data] += 1
        current = current.next

    # Delete nodes with duplicate values.
    for value, count in values.items():
        if count > 1:
            head_node = deleteNodeWithValue(head_node, value)

    return head_node


# Create linked list with duplicates
head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(3)
head.next.next.next.next = Node(2)

curr = head
while curr:
    print(curr.data, end="->")
    curr = curr.next
print("")

# Delete nodes with duplicated values
head = deleteDuplicateNodes(head)

# Print the new linked list
curr = head
while curr:
    print(curr.data, end="->")
    curr = curr.next
