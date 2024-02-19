def piece_value(piece):
    symbol = piece.symbol().upper()  # Convert to uppercase
    if symbol == 'P':  # pawn
        return 1
    elif symbol == 'N' or symbol == 'B':  # knight or bishop
        return 3
    elif symbol == 'R':  # rook or castle
        return 5
    elif symbol == 'Q':
        return 9
    elif symbol == 'K':
        return 100
    else:
        return 0
