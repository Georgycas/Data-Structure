class Node:
    def __init__(self, co_ef, exp):
        self.co_ef = co_ef
        self.exp = exp
        self.next = None


def add_term(poly, co_ef, exp):
    new_node = Node(co_ef, exp)
    if poly is None:
        return new_node
    current = poly
    prev = None
    while current is not None and current.exp > exp:
        prev = current
        current = current.next
    if current is not None and current.exp == exp:
        current.co_ef += co_ef
    else:
        new_node.next = current
        if prev is not None:
            prev.next = new_node
        else:
            poly = new_node
    return poly


def conv_LL(l, m):
    if l is None or m is None:
        return None
    search = None
    curr_l = l
    while curr_l is not None:
        curr_m = m
        while curr_m is not None:
            co_ef = curr_l.co_ef * curr_m.co_ef
            exp = curr_l.exp + curr_m.exp
            search = add_term(search, co_ef, exp)
            curr_m = curr_m.next
        curr_l = curr_l.next
    return search


# l = 1x^0 + 2x^2 + 3x^3 + 4x^5
l = Node(1, 0)
l = add_term(l, 2, 2)
l = add_term(l, 3, 3)
l = add_term(l, 4, 5)

# m = 5x^0 + 6x^1 + 7x^3 + 8x^4
m = Node(5, 0)
m = add_term(m, 6, 1)
m = add_term(m, 7, 3)
m = add_term(m, 8, 4)

# l * m = 5x^0 + 6x^1 + 10x^2 + 34x^3 + 26x^4 + 34x^5 + 61x^6 + 24x^7 + 28x^8 + 32x^9
result = conv_LL(l, m)

# print the result
curr = result
while curr is not None:
    print(f"{curr.co_ef}x^{curr.exp}", end=" + " if curr.next is not None else "")
    curr = curr.next
