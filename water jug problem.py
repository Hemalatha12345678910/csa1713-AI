from collections import deque

def water_jug_bfs(x, y, z):
    visited = set()
    queue = deque()

    # Each state is a tuple (amount_in_jug_x, amount_in_jug_y)
    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        a, b = queue.popleft()
        print(f"Jug A: {a} | Jug B: {b}")

        if a == z or b == z:
            print("Target reached!")
            return True

        # All possible next states
        next_states = [
            (x, b),     # Fill Jug A
            (a, y),     # Fill Jug B
            (0, b),     # Empty Jug A
            (a, 0),     # Empty Jug B
            (0, a + b) if a + b <= y else (a - (y - b), y),  # Pour A -> B
            (a + b, 0) if a + b <= x else (x, b - (x - a)),  # Pour B -> A
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("No solution.")
    return False

# Example: Jug A = 4L, Jug B = 3L, Target = 2L
water_jug_bfs(4, 3, 2)
