def find_safe_nests(n):
    # Create a circular linked list of 10 nests
    nests = [i + 1 for i in range(10)]
    current_nest = 0

    # Traverse the linked list and mark unsafe nests as None
    skip = 1
    for i in range(1, n + 1):
        # Skip nests
        for j in range(skip):
            current_nest = (current_nest + 1) % len(nests)
        skip += 1

        # Mark nest as unsafe
        nests[current_nest] = None

    # Return list of safe nests
    return [nest for nest in nests if nest is not None]


n = 5
safe_nests = find_safe_nests(n)
print(f"The safe nests after {n} wolf checks are: {safe_nests}")
