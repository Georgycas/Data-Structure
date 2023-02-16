class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def commElem(l, m):
    # convert linked list l to a set
    l_set = set()
    current_node = l.next
    while current_node:
        l_set.add(current_node.value)
        current_node = current_node.next

    # traverse linked list m and add common elements to result linked list
    result = Node(None) # dummy head node
    tail = result
    current_node = m.next
    while current_node:
        if current_node.value in l_set:
            new_node = Node(current_node.value)
            tail.next = new_node
            tail = new_node
        current_node = current_node.next

    # remove dummy head node and return result linked list
    result = result.next
    return result

# create linked list l
l = Node(None) # dummy head node
tail = l
for c in "GOOD":
    new_node = Node(c)
    tail.next = new_node
    tail = new_node

# create linked list m
m = Node(None) # dummy head node
tail = m
for c in "GoOGLE":
    new_node = Node(c)
    tail.next = new_node
    tail = new_node

# find common elements and create new linked list
result = commElem(l, m)

# print result linked list
current_node = result
while current_node:
    print(current_node.value, end="->")
    current_node = current_node.next
print("NULL")

