import pygame
from .player import Player
from .base_connect4 import Connect4
import math


class ConsoleHumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.gui_options = None

    def get_move(self, game: 'Connect4', piece: 'int'):
        while True:
            col = input("enter column index:")
            if col.isdigit():
                col = int(col)
                if 0 <= col < game.column_count:
                    return col
                else:
                    print(f"invalid input, please enter number from 0 to {game.column_count-1}")
            else:
                print("invalid input, please enter an integer")

