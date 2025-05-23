import math

def print_board(board):
    for i in range(3):
        print(board[3*i] + '|' + board[3*i+1] + '|' + board[3*i+2])
        if i < 2:
            print('-+-+-')

def is_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_conditions)

def is_board_full(board):
    return ' ' not in board

def alphabeta(board, depth, alpha, beta, is_maximizing):
    if is_winner(board, 'X'):
        return 10 - depth
    if is_winner(board, 'O'):
        return depth - 10
    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = alphabeta(board, depth + 1, alpha, beta, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cutoff
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = alphabeta(board, depth + 1, alpha, beta, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cutoff
        return min_eval

def best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = alphabeta(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Example usage:
board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']

print("Initial board:")
print_board(board)

move = best_move(board)
board[move] = 'X'

print(f"\nX plays at position {move}")
print_board(board)
