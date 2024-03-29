def create_positional_heatmap(piece):
    # Initial heatmap
    heatmap = [0.0 for _ in range(64)]
    symbol = piece.symbol().upper()

    if symbol == 'N':  # Knight
        heatmap = [
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
            0.00, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.00,
            0.00, 0.02, 0.06, 0.05, 0.05, 0.06, 0.02, 0.00,
            0.00, 0.03, 0.05, 0.10, 0.10, 0.05, 0.03, 0.00,
            0.00, 0.03, 0.05, 0.10, 0.10, 0.05, 0.03, 0.00,
            0.00, 0.02, 0.06, 0.05, 0.05, 0.06, 0.02, 0.00,
            0.00, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.00,
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00
        ]
    # elif symbol == 'P':  # Pawn
    #     heatmap = create_pawn_heatmap(piece.color)
    elif symbol == 'B':  # Bishop
        heatmap = [
            0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.02,
            0.01, 0.05, 0.03, 0.03, 0.03, 0.03, 0.05, 0.01,
            0.01, 0.03, 0.07, 0.05, 0.05, 0.07, 0.03, 0.01,
            0.01, 0.03, 0.05, 0.10, 0.10, 0.05, 0.03, 0.01,
            0.01, 0.03, 0.05, 0.10, 0.10, 0.05, 0.03, 0.01,
            0.01, 0.03, 0.07, 0.05, 0.05, 0.07, 0.03, 0.01,
            0.01, 0.05, 0.03, 0.03, 0.03, 0.03, 0.05, 0.01,
            0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.02
        ]
    # elif symbol == 'K':  # King
    #     heatmap = create_king_heatmap(piece.color)

    return heatmap

def create_pawn_heatmap(color):
    pawn_values = []
    if color == False:
        pawn_values = [ 
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
            0.02, 0.01, 0.00, 0.00, 0.00, 0.00, 0.01, 0.02,
            0.01, 0.01, 0.03, 0.06, 0.06, 0.03, 0.01, 0.01,
            0.02, 0.02, 0.04, 0.07, 0.07, 0.04, 0.02, 0.02,
            0.03, 0.03, 0.05, 0.08, 0.08, 0.05, 0.03, 0.03,
            0.07, 0.07, 0.08, 0.09, 0.09, 0.08, 0.07, 0.07,
            0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10,
            9.00, 9.00, 9.00, 9.00, 9.00, 9.00, 9.00, 9.00,
        ]
    elif color == True:
        pawn_values = [ 
            9.00, 9.00, 9.00, 9.00, 9.00, 9.00, 9.00, 9.00,
            0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10,
            0.07, 0.07, 0.08, 0.09, 0.09, 0.08, 0.07, 0.07,
            0.03, 0.03, 0.05, 0.08, 0.08, 0.05, 0.03, 0.03,
            0.02, 0.02, 0.04, 0.07, 0.07, 0.04, 0.02, 0.02,
            0.01, 0.01, 0.03, 0.06, 0.06, 0.03, 0.01, 0.01,
            0.02, 0.01, 0.00, 0.00, 0.00, 0.00, 0.01, 0.02,
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
        ]
    return pawn_values

def create_king_heatmap(color):
    heatmap = []
    if color == False:
        heatmap = [ 
            0.05, 0.50, 0.10, 0.00, 0.00, 0.00, 0.10, 0.05,
            0.02, 0.02, 0.00, 0.00, 0.00, 0.00, 0.02, 0.02,
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
        ]
    elif color == True:
        heatmap = [ 
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
            0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00,
            0.02, 0.02, 0.00, 0.00, 0.00, 0.00, 0.02, 0.02,
            0.05, 0.50, 0.10, 0.00, 0.00, 0.00, 0.10, 0.05,
        ]
    return heatmap