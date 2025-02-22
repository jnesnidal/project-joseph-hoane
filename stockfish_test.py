"""
File: stockfish_test.py
Author: John Nesnidal

Ubuntu users should run these two commands (as root) before running:
pip install stockfish
apt install stockfish
"""

import stockfish

fish = stockfish.Stockfish()

# Set this variable to True for white's pov, False for black's POV
POV_WHITE = False

print(fish.get_parameters())
print()
print("BOARD CONFIGURATION (start of game, from white's POV)")
print("White is represented as UPPERCASE")
print("Black is represented as lowercase")
print(fish.get_board_visual(POV_WHITE)) # True for white's POV, False for black's POV