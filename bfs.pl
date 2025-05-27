% Define edges of the graph (undirected for simplicity)
edge(a, b).
edge(a, c).
edge(b, d).
edge(c, d).
edge(c, e).
edge(d, f).
edge(e, f).

% Define heuristic values for each node
heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 4).
heuristic(d, 2).
heuristic(e, 1).
heuristic(f, 0).  % Goal node
