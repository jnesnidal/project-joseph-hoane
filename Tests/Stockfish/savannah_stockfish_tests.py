"""
    File: savannah_stockfish_tests.py
    Author: Savannah Franklin
    nedid: sf03 (@iastate.edu)

"""

import stockfish

POV_WHITE = True

def checkmate_demo():
    fish = stockfish.Stockfish()
    print("Initial board:")
    print(fish.get_board_visual(POV_WHITE))

    #Fool's Mate
    moves = [
        "f2f3",  # White moves pawn
        "e7e5",  # Black moves pawn
        "g2g4",  # White moves pawn
        "d8h4",  # Black moves queen
    ]

    # Execute the move sequence
    fish.make_moves_from_current_position(moves)

    print("Final board after checkmate:")
    print(fish.get_board_visual(POV_WHITE))


def invalid_move_demo():
    fish = stockfish.Stockfish()
    print("Initial board:")
    print(fish.get_board_visual(POV_WHITE))

    # try moving backwards
    invalid_move = "e2e1"  # White moves pawn

    try:
        fish.make_moves_from_current_position([invalid_move])
        print("Invalid move was accepted (this should not happen).")
    except Exception as e:
        print(f"Error occurred: {e}")

    print("Final board (should be unchanged):")
    print(fish.get_board_visual(POV_WHITE))

checkmate_demo()
invalid_move_demo()