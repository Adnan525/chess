def check_central_control(piece, square):
    central_control_bonus = 0
    if square in [27, 28, 35, 36]:
        if piece.symbol() in ["N", "B"]:
            central_control_bonus += 0.5
        elif piece.symbol() in ["R", "Q"]:
            central_control_bonus += 0.8
        else:
            central_control_bonus += 0.2
    
    return central_control_bonus