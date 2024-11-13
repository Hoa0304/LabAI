def minimax(board, depth, is_maximizing):
    scores = {'X': 1, 'O': -1, 'Tie': 0}
    result = check_winner(board)
    if result:
        return scores[result]
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ''
                    best_score = min(score, best_score)
        return best_score

def check_winner(board):
    return None

board = [['', '', ''], ['', '', ''], ['', '', '']]
print("Best score for the starting position:", minimax(board, 0, True))

## =================================================================

import math

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner:
        return 1 if winner == 'X' else -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score
