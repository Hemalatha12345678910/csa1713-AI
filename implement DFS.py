def dfs_recursive(graph, node, visited=None, traversal_order=None):
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []

    visited.add(node)
    traversal_order.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, traversal_order)
    
    return traversal_order

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Run DFS
print("DFS Traversal (Recursive):", dfs_recursive(graph, 'A'))

