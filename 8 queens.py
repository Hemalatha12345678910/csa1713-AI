N = 8

def is_safe(board, row, col):
    # Check this column on the upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row):
    if row == N:
        print_solution(board)
        return True  # Return True to find just one solution
        # return False  # Use this instead if you want *all* solutions

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = 0  # Backtrack
    return False

def print_solution(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print("\n" + "-"*16)

# Initialize 8x8 board with zeros
board = [[0 for _ in range(N)] for _ in range(N)]

# Solve and print one solution
solve_n_queens(board, 0)
