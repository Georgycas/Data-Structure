class Node:
    def __init__(self, val=''):
        self.val = val
        self.next = None


def sortLinkedList(head_node):
    # Use a dictionary to count the occurrence of each character
    char_counts = {}
    current = head_node
    while current:
        char_counts[current.val] = char_counts.get(current.val, 0) + 1
        current = current.next

    # Create a new linked list with the characters in sorted order
    new_head_node = None
    for char in sorted(char_counts.keys()):
        for i in range(char_counts[char]):
            new_node = Node(char)
            new_node.next = new_head_node
            new_head_node = new_node

    return new_head_node


# Create a linked list
head = Node('D')
head.next = Node('A')
head.next.next = Node('C')
head.next.next.next = Node('A')
head.next.next.next.next = Node('G')

# Print unsorted linked list
curr = head
while curr:
    print(curr.val, end="->")
    curr = curr.next
print("")

# Sort the linked list
new_head = sortLinkedList(head)

# Print the sorted linked list
curr = new_head
while curr:
    print(curr.val, end="->")
    curr = curr.next
