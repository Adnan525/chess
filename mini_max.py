import chess
import math
from board_eval import evaluate_board


def generate_moves(board, color):
    legal_moves = list(board.legal_moves)
    if color : # white
        return [move for move in legal_moves if chess.WHITE == board.color_at(move.from_square)]
    else: # black
        return [move for move in legal_moves if chess.BLACK == board.color_at(move.from_square)]
    
def mini_max(board, depth, color):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board, color), None
    all_moves = generate_moves(board, color)
    best_move = all_moves[0]
    if color: # white
        max_eval = -math.inf
        for move in all_moves:
            board.push(move)
            eval_val, _ = mini_max(board, depth - 1, not color)
            board.pop()
            if eval_val > max_eval:
                max_eval = eval_val
                best_move = move
        return max_eval, best_move
    else: # black
        min_eval = math.inf
        for move in all_moves:
            board.push(move)
            eval_val, _ = mini_max(board, depth - 1, not color)
            board.pop()
            if eval_val < min_eval:
                min_eval = eval_val
                best_move = move
        return min_eval, best_move


# def autoplay():
#     board = chess.Board()
#     while not board.is_game_over():
#         if board.turn == chess.WHITE:
#             move = minimax(board, depth=3)
#         else:
#             move = minimax(board, depth=3)
#         board.push(move)
#         print(board)
#         print()
#     print(board)
#     print("Game Over")
#     print("Result:", board.result())

# autoplay()
