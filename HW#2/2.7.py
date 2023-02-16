class Node:
    def __init__(self, coef, exp):
        self.coef = coef
        self.exp = exp
        self.next = None

def add_term(poly, coef, exp):
    new_node = Node(coef, exp)
    if poly is None:
        return new_node
    curr = poly
    prev = None
    while curr is not None and curr.exp > exp:
        prev = curr
        curr = curr.next
    if curr is not None and curr.exp == exp:
        curr.coef += coef
    else:
        new_node.next = curr
        if prev is not None:
            prev.next = new_node
        else:
            poly = new_node
    return poly

def conv_LL(l, m):
    if l is None or m is None:
        return None
    result = None
    curr_l = l
    while curr_l is not None:
        curr_m = m
        while curr_m is not None:
            coef = curr_l.coef * curr_m.coef
            exp = curr_l.exp + curr_m.exp
            result = add_term(result, coef, exp)
            curr_m = curr_m.next
        curr_l = curr_l.next
    return result

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
    print(f"{curr.coef}x^{curr.exp}", end=" + " if curr.next is not None else "")
    curr = curr.next
