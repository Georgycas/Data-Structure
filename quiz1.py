class Node:
    """ A singly-linked node. """

    def __init__(self, data=None):
        self.data = data
        self.next = None


def is_element_in_LL(head: Node, value) -> bool:
    current = head

    while current:
        if current.data == value:
            return True
        current = current.next

    return False

# create a linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

# check if 3 is in the linked list
result = is_element_in_LL(head, 3)
print(result)  # output: True

# check if 5 is in the linked list
result = is_element_in_LL(head, 5)
print(result)  # output: False
