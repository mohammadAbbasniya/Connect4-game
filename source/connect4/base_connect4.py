import sys
import numpy as np


class Connect4:
    def __init__(self, row_count, column_count, board=None):
        self.row_count = row_count
        self.column_count = column_count
        if board is None:
            self.board = np.zeros((row_count, column_count))
        else:
            self.board = board

    def opposite_piece(self, piece):
        if piece == 1:
            return 2
        elif piece == 2:
            return 1

    def drop_piece(self, col, piece):
        for r in range(self.row_count):
            if self.board[r][col] == 0:
                self.board[r][col] = piece
                return
        sys.exit("invalid drop on column:" + str(col) + " with piece:" + str(piece))

    def is_valid_location(self, col):
        return self.board[self.row_count - 1][col] == 0

    def winning_move(self, piece):
        # Check horizontal locations for win
        for c in range(self.column_count - 3):
            for r in range(self.row_count):
                if self.board[r][c] == piece and \
                        self.board[r][c + 1] == piece and \
                        self.board[r][c + 2] == piece and \
                        self.board[r][c + 3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(self.column_count):
            for r in range(self.row_count - 3):
                if self.board[r][c] == piece and \
                        self.board[r + 1][c] == piece and \
                        self.board[r + 2][c] == piece and \
                        self.board[r + 3][c] == piece:
                    return True

        # Check positively sloped diaganols
        for c in range(self.column_count - 3):
            for r in range(self.row_count - 3):
                if self.board[r][c] == piece and \
                        self.board[r + 1][c + 1] == piece and \
                        self.board[r + 2][c + 2] == piece and \
                        self.board[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diaganols
        for c in range(self.column_count - 3):
            for r in range(3, self.row_count):
                if self.board[r][c] == piece and \
                        self.board[r - 1][c + 1] == piece and \
                        self.board[r - 2][c + 2] == piece and \
                        self.board[r - 3][c + 3] == piece:
                    return True

    def get_valid_locations(self):
        res = []
        for i in range(self.column_count):
            if self.is_valid_location(i):
                res.append(i)
        return res

    def is_terminal_node(self):
        return self.winning_move(1) or \
               self.winning_move(2) or \
               len(self.get_valid_locations()) == 0

    def copy(self):
        copy_board = self.board.copy()
        copy_game = Connect4(self.row_count, self.column_count, copy_board)
        return copy_game
