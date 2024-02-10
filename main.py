import chess
import math

# def clear_screen():
#     # if windows then will return "nt" so use cls to clear the screen
#     # if linux then will return "posix" so use clear to clear the screen
#     os.system('cls' if os.name == 'nt' else 'clear')

def evaluate_board(board):
    # simplest evaluation function, just summing up the piece values
    return sum(piece_value(piece) for piece in board.piece_map().values())

def piece_value(piece):
    if piece.symbol() == 'P':
        return 1
    elif piece.symbol() == 'N' or piece.symbol() == 'B':
        return 3
    elif piece.symbol() == 'R':
        return 5
    elif piece.symbol() == 'Q':
        return 9
    elif piece.symbol() == 'K':
        return 100
    else:
        return 0

def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing_player:
        max_eval = -math.inf
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop() # undo the last move
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def find_best_move(board, depth, maximizing_player):
    best_move = None
    if maximizing_player:
        max_eval = -math.inf
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, -math.inf, math.inf, False)
            print(f"maximizing_player: {move} score {eval}")
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            print(f"maximizing_player: {best_move} score {max_eval}")
    else:
        min_eval = math.inf
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, -math.inf, math.inf, True)
            print(f"minimizing_player: {move} score {eval}")
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            print(f"minimizing_player: {best_move} score {min_eval}")             
    return best_move

def auto_play(board, depth):
    while not board.is_game_over():
        if board.turn == chess.WHITE:
            move = find_best_move(board, depth, True)
        else:
            move = find_best_move(board, depth, False)
        board.push(move)
        print(board)
    print("Game Over")
    print("Result: " + board.result())

def main():
    board = chess.Board()

    print("Welcome to Chess!")
    print("Automatic play with Minimax algorithm")

    depth = 3
    auto_play(board, depth)

if __name__ == "__main__":
    main()
