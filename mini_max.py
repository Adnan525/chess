import chess
from board_eval import evaluate_board


def generate_moves(board):
    return list(board.legal_moves)

def min_value(board, depth, alpha, beta):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    min_val = float('inf')
    for move in generate_moves(board):
        board.push(move)
        min_val = min(min_val, max_value(board, depth - 1, alpha, beta))
        board.pop()
        if min_val <= alpha:
            return min_val
        beta = min(beta, min_val)
    return min_val

def max_value(board, depth, alpha, beta):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    max_val = float('-inf')
    for move in generate_moves(board):
        board.push(move)
        max_val = max(max_val, min_value(board, depth - 1, alpha, beta))
        board.pop()
        if max_val >= beta:
            return max_val
        alpha = max(alpha, max_val)
    return max_val

def minimax(board, depth):
    best_move = None
    max_eval = float('-inf')
    alpha = float('-inf')
    beta = float('inf')
    for move in generate_moves(board):
        board.push(move)
        eval_val = min_value(board, depth - 1, alpha, beta)
        board.pop()
        if eval_val > max_eval:
            max_eval = eval_val
            best_move = move
    print(f"Best move: {best_move} with eval: {max_eval}")
    return best_move

def autoplay():
    board = chess.Board()
    while not board.is_game_over():
        if board.turn == chess.WHITE:
            move = minimax(board, depth=3)
        else:
            move = minimax(board, depth=3)
        board.push(move)
        print(board)
        print()
    print(board)
    print("Game Over")
    print("Result:", board.result())

autoplay()
