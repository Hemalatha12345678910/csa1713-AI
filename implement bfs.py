from collections import deque

def bfs(graph, start):
    visited = set()           # To keep track of visited nodes
    queue = deque([start])    # Use deque for efficient pops from the left

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')  # Process the node
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

# Example graph (undirected)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Perform BFS starting from node 'A'
print("BFS traversal starting from node A:")
bfs(graph, 'A')
