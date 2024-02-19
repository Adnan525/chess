import chess
from board_eval import evaluate_board

def print_board(board):
    print(board)

def get_move(board):
    while True:
        try:
            move_str = input("Enter your move (e.g., e2e4): ")
            move = chess.Move.from_uci(move_str)
            if move in board.legal_moves:
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid move format. Try again.")

def play_game():
    board = chess.Board()
    print("Welcome to Chess!")
    print_board(board)

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            print(f"eval: {evaluate_board(board, True)}")
            print("White's turn")
        else:
            print("Black's turn")
            print(f"eval: {evaluate_board(board, False)}")

        move = get_move(board)
        board.push(move)
        print_board(board)

    print("Game Over")
    print("Result:", board.result())

if __name__ == "__main__":
    play_game()
