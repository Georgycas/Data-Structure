class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteLLNode(head_node, search):
    # Handle the case where the head node has the target value.
    while head_node and head_node.data == search:
        head_node = head_node.next

    current = head_node
    while current and current.next:
        if current.next.data == search:
            current.next = current.next.next
        else:
            current = current.next

    return head_node


# Create linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(3)

# Print the new linked list
curr = head
while curr:
    print(curr.data, end="->")
    curr = curr.next

print("")

# Delete nodes with value 1
head = deleteLLNode(head, 1)

# Print the new linked list
curr = head
while curr:
    print(curr.data, end="->")
    curr = curr.next
