from piece_value import piece_value
from positional_advantage import create_positional_heatmap
from bonus import check_central_control

def evaluate_board(board, color):
    total_eval = 0

    # Iterate over all pieces on the board
    for square, piece in board.piece_map().items():
        # Add piece value
        # True for white, false for black
        if piece.color == color:
            total_eval += piece_value(piece)
            # print(f"piece eval {piece, piece_value(piece)}")

            # Add positional heatmap value
            piece_heatmap = create_positional_heatmap(piece)
            if piece.color == True:
                total_eval += piece_heatmap[square]
                # print(f"positional val {square, piece_heatmap[square]}")
            elif piece.color == False:
                # Invert the board for black pieces
                total_eval += piece_heatmap[square]
                # print(f"positional val {square, piece_heatmap[square]}")

            # Add central control bonus
            total_eval += check_central_control(piece, square)    

    return round(total_eval, 2)

