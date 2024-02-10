import chess
import math
import os

def clear_screen():
    # if windows then will return "nt" so use cls to clear the screen
    # if linux then will return "posix" so use clear to clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    clear_screen()
    print(board)

def evaluate_board(board):
    # simplest eval function: just sum the piece values
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
            board.pop()
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

def find_best_move(board, depth):
    best_move = None
    max_eval = -math.inf
    alpha = -math.inf
    beta = math.inf

    for move in board.legal_moves:
        board.push(move)
        eval = minimax(board, depth - 1, alpha, beta, False)
        board.pop()
        if eval > max_eval:
            max_eval = eval
            best_move = move
    return best_move

def main():
    board = chess.Board()

    print("Welcome to Chess!")
    print("Enter your moves in algebraic notation (e.g., e2e4)")

    while not board.is_game_over():
        print_board(board)

        if board.turn == chess.WHITE:
            move = input("Enter your move: ")
            try:
                board.push_san(move)
            except ValueError:
                print("Invalid move, please try again.")
                continue
        else:
            depth = 3  # Adjust the depth according to your preference
            best_move = find_best_move(board, depth)
            print("Opponent's move:", best_move)
            board.push(best_move)

    print("Game Over")
    print("Result: " + board.result())

if __name__ == "__main__":
    main()