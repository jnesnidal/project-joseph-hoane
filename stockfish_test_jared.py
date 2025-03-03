import stockfish

POV_WHITE = True


def best_move_demo():
    fish = stockfish.Stockfish()

    print("BOARD CONFIGURATION (start of game, from white's POV)")
    print("White is represented as UPPERCASE")
    print("Black is represented as lowercase")
    print(fish.get_board_visual(POV_WHITE))
    # White moves once
    move_w1 = fish.get_best_move()
    print(move_w1)
    fish.make_moves_from_current_position([move_w1])
    print(fish.get_board_visual(POV_WHITE))

    # Black moves once
    move_b1 = fish.get_best_move()
    print(move_b1)
    fish.make_moves_from_current_position([move_b1])
    print(fish.get_board_visual(POV_WHITE))


def castling_demo():
    fish = stockfish.Stockfish()
    fish.make_moves_from_current_position(["e2e4"])
    fish.make_moves_from_current_position(["e7e5"])

    fish.make_moves_from_current_position(["f1c4"])
    fish.make_moves_from_current_position(["f8c5"])

    fish.make_moves_from_current_position(["g1f3"])
    fish.make_moves_from_current_position(["g8f6"])

    print("Before castling:")
    print(fish.get_board_visual(POV_WHITE))

    # Castling (kingside) in stockfish is represented by the king attempting to move two squares toward the king side
    fish.make_moves_from_current_position(["e1g1"])

    print("After castling:")
    print(fish.get_board_visual(POV_WHITE))


# castling_demo()


def pawn_promotion_demo():
    fish = stockfish.Stockfish()
    print(fish.get_board_visual(POV_WHITE))

    moves = [
        "b2b3",
        "g8f6",
        "c2c3",
        "f6g8",
        "b3b4",
        "g8f6",
        "c3c4",
        "f6g8",
        "b4b5",
        "g8f6",
        "c4c5",
        "f6g8",
        "c5c6",
        "b7c6",
        "b5b6",
        "c6c5",
        "b6b7",
        "b8c6",
        "b7b8q",

    ]

    # Execute the entire move sequence.
    fish.make_moves_from_current_position(moves)

    print("Final board after simulation (white pawn promoted):")
    print(fish.get_board_visual(POV_WHITE))


pawn_promotion_demo()