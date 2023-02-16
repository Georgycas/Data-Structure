class Node:
    def __init__(self, val='', next=None):
        self.val = val
        self.next = next


def sortLinkedList(head):
    # Use a dictionary to count the occurrence of each character
    char_counts = {}
    curr = head
    while curr:
        char_counts[curr.val] = char_counts.get(curr.val, 0) + 1
        curr = curr.next

    # Create a new linked list with the characters in sorted order
    new_head = None
    for char in sorted(char_counts.keys()):
        for i in range(char_counts[char]):
            new_node = Node(char)
            new_node.next = new_head
            new_head = new_node

    return new_head

# Create a linked list
head = Node('D')
head.next = Node('A')
head.next.next = Node('C')
head.next.next.next = Node('A')
head.next.next.next.next = Node('G')

# Sort the linked list
new_head = sortLinkedList(head)

# Print the sorted linked list
curr = new_head
while curr:
    print(curr.val, end="->")
    curr = curr.next
