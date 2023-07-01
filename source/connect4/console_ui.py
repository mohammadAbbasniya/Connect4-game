import numpy as np
from .base_connect4 import Connect4
from .player import Player
from .player_human_graphical import GraphicalHumanPlayer
from .player_ai import AIPlayer


class ConsoleUI:
    def __init__(self, rows, cols, player1: 'Player', player2: 'Player'):
        self.rows = rows
        self.cols = cols
        self.game = Connect4(row_count=rows, column_count=cols)

        assert player1.__class__ != GraphicalHumanPlayer, "Graphical human player can't play in ConsoleUI"
        assert player2.__class__ != GraphicalHumanPlayer, "Graphical human player can't play in ConsoleUI"
        self.player1 = player1
        self.player2 = player2

    def print_board(self):
        print()
        print(np.flip(self.game.board, 0))

    def start(self):
        self.print_board()
        turn_flag = True

        while True:
            if turn_flag:  # player 1
                if self.player1.__class__ is AIPlayer:
                    print("AI is thinking...")

                col = self.player1.get_move(self.game, 1)
                if col == -1:
                    return

                self.game.drop_piece(col, 1)
                if self.game.winning_move(1):
                    self.print_board()
                    print('Player 1 Won !!!')
                    break

            else:  # player 2
                if self.player2.__class__ is AIPlayer:
                    print("AI is thinking...")

                col = self.player2.get_move(self.game, 2)
                if col == -1:
                    return

                self.game.drop_piece(col, 2)
                if self.game.winning_move(2):
                    self.print_board()
                    print('Player 2 Won !!!')
                    break

            self.print_board()
            turn_flag = not turn_flag
