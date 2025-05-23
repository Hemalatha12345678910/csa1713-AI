def minimax(depth, node_index, is_maximizing, values, branching_factor):
    # Base case: reached bottom of the tree
    if depth == 0:
        return values[node_index]

    if is_maximizing:
        best = float('-inf')
        for i in range(branching_factor):
            val = minimax(depth - 1, node_index * branching_factor + i, False, values, branching_factor)
            best = max(best, val)
        return best
    else:
        best = float('inf')
        for i in range(branching_factor):
            val = minimax(depth - 1, node_index * branching_factor + i, True, values, branching_factor)
            best = min(best, val)
        return best

# Example: depth = 3, branching factor = 2, leaf values = game outcomes
values = [3, 5, 2, 9, 12, 5, 23, 23]  # 2^3 = 8 leaves
depth = 3
branching_factor = 2

optimal_value = minimax(depth, 0, True, values, branching_factor)
print(f"Optimal value is: {optimal_value}")
