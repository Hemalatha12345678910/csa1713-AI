import itertools

# Distance matrix (symmetric)
# Example: 4 cities
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def tsp_brute_force(dist_matrix):
    n = len(dist_matrix)
    cities = list(range(n))
    min_path = None
    min_cost = float('inf')

    for perm in itertools.permutations(cities[1:]):  # fix city 0 as the start
        path = [0] + list(perm) + [0]
        cost = sum(dist_matrix[path[i]][path[i+1]] for i in range(n))
        if cost < min_cost:
            min_cost = cost
            min_path = path

    return min_path, min_cost

path, cost = tsp_brute_force(distances)
print("Minimum cost path:", path)
print("Total cost:", cost)
