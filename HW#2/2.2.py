class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def LL_add(u, v):
    # Reverse the linked lists
    u = reverseLinkedList(u)
    v = reverseLinkedList(v)

    # Add the numbers
    carry = 0
    sum_list = None
    while u or v or carry:
        u_val = u.val if u else 0
        v_val = v.val if v else 0
        digit_sum = u_val + v_val + carry
        carry = digit_sum // 10
        digit = digit_sum % 10
        new_node = Node(digit)
        new_node.next = sum_list
        sum_list = new_node
        if u:
            u = u.next
        if v:
            v = v.next

    # Reverse the sum list and return the head node
    return reverseLinkedList(sum_list)


def reverseLinkedList(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

# Create the input linked lists
u = Node(1)
u.next = Node(2)
u.next.next = Node(3)
u.next.next.next = Node(4)

v = Node(5)
v.next = Node(6)
v.next.next = Node(7)
v.next.next.next = Node(8)

# Add the linked lists
sum_list = LL_add(u, v)

# Print the sum linked list
curr = sum_list
while curr:
    print(curr.val, end="->")
    curr = curr.next
