import stockfish

POV_WHITE = True  # Whether to display the board from White's perspective


def initialize_stockfish():
    """Initialize Stockfish engine."""
    return stockfish.Stockfish()


def display_board(fish, message="Board State:"):
    """Displays the chess board from the given point of view."""
    print(f"\n{message}")
    print(fish.get_board_visual(POV_WHITE))


def best_move_sequence():
    """Demonstrates Stockfish making the best moves for both players."""
    fish = initialize_stockfish()

    display_board(fish, "Initial Board Configuration")

    # White's best move
    move_w1 = fish.get_best_move()
    print(f"White moves: {move_w1}")
    fish.make_moves_from_current_position([move_w1])
    display_board(fish, "After White's Move")

    # Black's best response
    move_b1 = fish.get_best_move()
    print(f"Black moves: {move_b1}")
    fish.make_moves_from_current_position([move_b1])
    display_board(fish, "After Black's Move")


def castling_example():
    """Demonstrates castling in Stockfish."""
    fish = initialize_stockfish()

    moves = ["e2e4", "e7e5", "g1f3", "b8c6", "f1e2", "g8f6", "e1g1"]  # Kingside castling
    fish.make_moves_from_current_position(moves)

    display_board(fish, "After Kingside Castling (White)")


def pawn_promotion_example():
    """Demonstrates pawn promotion in Stockfish."""
    fish = initialize_stockfish()

    moves = [
        "b2b3", "g8f6", "c2c3", "f6g8",
        "b3b4", "g8f6", "c3c4", "f6g8",
        "b4b5", "g8f6", "c4c5", "f6g8",
        "c5c6", "b7c6", "b5b6", "c6c5",
        "b6b7", "b8c6", "b7b8q",  # Promotion to queen
    ]
    fish.make_moves_from_current_position(moves)

    display_board(fish, "Final Board after Pawn Promotion")


def en_passant_example():
    """Demonstrates en passant move."""
    fish = initialize_stockfish()

    moves = [
        "e2e4", "a7a5",
        "e4e5", "d7d5",  # Black advances pawn two squares
        "e5d6"  # White captures en passant
    ]
    fish.make_moves_from_current_position(moves)

    display_board(fish, "After En Passant Capture")


# Run demonstrations
best_move_sequence()
castling_example()
pawn_promotion_example()
en_passant_example()
