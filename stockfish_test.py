"""
File: stockfish_test.py
Author: John Nesnidal

Ubuntu users should run these two commands (as root) before running:
pip install stockfish
apt install stockfish
"""

import stockfish

# Set this variable to True for white's pov, False for black's POV
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

castling_demo()