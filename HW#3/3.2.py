class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def find_common_nodes(l, m):
    # Find the start node of each circular linked list
    l_start = l
    while l_start.val <= l.val:
        l_start = l_start.next
        if l_start == l:
            break

    m_start = m
    while m_start.val <= m.val:
        m_start = m_start.next
        if m_start == m:
            break

    # Traverse the linked lists and find common values
    common_values = set()
    while True:
        if l.val == m.val:
            common_values.add(l.val)

        l = l.next
        if l == l_start:
            break

        m = m.next
        if m == m_start:
            break

    # Create a new circular linked list with common values
    new_list = None
    tail = None
    for val in sorted(common_values):
        if new_list is None:
            new_list = Node(val)
            tail = new_list
        elif val != tail.val:
            new_node = Node(val)
            tail.next = new_node
            tail = new_node
        tail.next = new_list

    return new_list


# Create circular linked lists l and m
l = Node('a')
l.next = Node('b')
l.next.next = Node('c')
l.next.next.next = Node('f')
l.next.next.next.next = Node('g')
l.next.next.next.next.next = l

m = Node('b')
m.next = Node('c')
m.next.next = Node('d')
m.next.next.next = Node('f')
m.next.next.next.next = Node('h')
m.next.next.next.next.next = m

# Find common nodes
common_list = find_common_nodes(l, m)

# Print the common nodes
if common_list is None:
    print("No common nodes")
else:
    current = common_list
    while current.next != common_list:
        print(current.val, end=" ")
        current = current.next
    print(current.val)
