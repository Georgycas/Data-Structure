class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteLinkedListNode(head, key):
    # Handle the case where the head node has the target value.
    while head and head.val == key:
        head = head.next

    curr = head
    while curr and curr.next:
        if curr.next.val == key:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head


# Create linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(3)

# Delete nodes with value 1
head = deleteLinkedListNode(head, 1)

# Print the new linked list
curr = head
while curr:
    print(curr.val, end="->")
    curr = curr.next
