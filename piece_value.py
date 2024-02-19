def piece_value(piece):
    if piece.symbol() == 'P': # pawn
        return 1
    elif piece.symbol() == 'N' or piece.symbol() == 'B': # knight or bishop
        return 3
    elif piece.symbol() == 'R': # rook or castle
        return 5
    elif piece.symbol() == 'Q':
        return 9
    elif piece.symbol() == 'K':
        return 100