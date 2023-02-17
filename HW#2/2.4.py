class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def commElem(l, m):
    # convert linked list l to a set
    l_set = set()
    current = l.next
    while current:
        l_set.add(current.value)
        current = current.next

    # traverse linked list m and add common elements to result linked list
    search = Node(None)  # dummy head node
    tail = search
    current = m.next
    while current:
        if current.value in l_set:
            dif_node = Node(current.value)
            tail.next = dif_node
            tail = dif_node
        current = current.next

    # remove dummy head node and return result linked list
    search = search.next
    return search


# create linked list l
l = Node(None)  # dummy head node
tails = l
for c in "GOOD":
    new_node = Node(c)
    tails.next = new_node
    tails = new_node

# create linked list m
m = Node(None)  # dummy head node
tails = m
for c in "GoOGLE":
    new_node = Node(c)
    tails.next = new_node
    tails = new_node

# find common elements and create new linked list
result = commElem(l, m)

# print result linked list
current_node = result
while current_node:
    print(current_node.value, end="->")
    current_node = current_node.next
print("NULL")
