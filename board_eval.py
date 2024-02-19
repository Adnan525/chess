from piece_value import piece_value
from positional_advantage import create_positional_heatmap
from bonus import check_central_control

def evaluate_board(board):
    total_eval = 0

    # Iterate over all pieces on the board
    for square, piece in board.piece_map().items():
        # Add piece value
        total_eval += piece_value(piece)

        # Add positional heatmap value
        piece_heatmap = create_positional_heatmap(piece)
        if piece.color == 'white':
            total_eval += piece_heatmap[square[0]][square[1]]
        elif piece.color == 'black':
            # Invert the board for black pieces
            total_eval += piece_heatmap[7 - square[0]][7 - square[1]]

        # Add central control bonus
        total_eval += check_central_control(piece, square)    

    return total_eval

