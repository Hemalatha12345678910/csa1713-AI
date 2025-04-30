import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.priority = self.moves + self.manhattan_distance()

    def manhattan_distance(self):
        distance = 0
        for i, val in enumerate(self.board):
            if val == 0:
                continue
            x, y = divmod(i, 3)
            goal_x, goal_y = divmod(val - 1, 3)
            distance += abs(x - goal_x) + abs(y - goal_y)
        return distance

    def is_goal(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def get_neighbors(self):
        neighbors = []
        zero_index = self.board.index(0)
        x, y = divmod(zero_index, 3)
        directions = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_x * 3 + new_y
                new_board = self.board[:]
                new_board[zero_index], new_board[new_index] = new_board[new_index], new_board[zero_index]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
        return neighbors

    def __lt__(self, other):
        return self.priority < other.priority

def solve_8_puzzle(start_board):
    start = PuzzleState(start_board)
    frontier = []
    heapq.heappush(frontier, start)
    visited = set()

    while frontier:
        current = heapq.heappop(frontier)
        if current.is_goal():
            return reconstruct_path(current)

        visited.add(tuple(current.board))

        for neighbor in current.get_neighbors():
            if tuple(neighbor.board) not in visited:
                heapq.heappush(frontier, neighbor)

    return None

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.previous
    return path[::-1]

# Example usage:
initial_state = [1, 2, 3,
                 4, 0, 6,
                 7, 5, 8]

solution = solve_8_puzzle(initial_state)
if solution:
    for step in solution:
        print(step[:3])
        print(step[3:6])
        print(step[6:])
        print("-----")
else:
    print("No solution found.")
