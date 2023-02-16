class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def diffElem_LL(l, m):
    # Create sets to store char values of each linked list
    set_l = set()
    set_m = set()

    # Traverse linked list l and add its char values to set_l
    ptr_l = l
    while ptr_l:
        set_l.add(ptr_l.val)
        ptr_l = ptr_l.next

    # Traverse linked list m and add its char values to set_m
    ptr_m = m
    while ptr_m:
        set_m.add(ptr_m.val)
        ptr_m = ptr_m.next

    # Create a new linked list to store non-common char values
    head = Node()
    ptr = head

    # Traverse linked list l and add its non-common char values to the new linked list
    ptr_l = l
    while ptr_l:
        if ptr_l.val not in set_m:
            ptr.next = Node(ptr_l.val)
            ptr = ptr.next
        ptr_l = ptr_l.next

    # Traverse linked list m and add its non-common char values to the new linked list
    ptr_m = m
    while ptr_m:
        if ptr_m.val not in set_l:
            ptr.next = Node(ptr_m.val)
            ptr = ptr.next
        ptr_m = ptr_m.next

    return head.next

# Create linked list l with char type nodes
l = Node("G")
l.next = Node("O")
l.next.next = Node("O")
l.next.next.next = Node("D")

# Create linked list m with char type nodes
m = Node("G")
m.next = Node("o")
m.next.next = Node("O")
m.next.next.next = Node("g")
m.next.next.next.next = Node("L")
m.next.next.next.next.next = Node("E")

# Call diffElem_LL function to get a new linked list with non-common char values
result = diffElem_LL(l, m)

# Traverse the new linked list and print its char values
ptr = result
while ptr:
    print(ptr.val, end="->")
    ptr = ptr.next
print("NULL")
