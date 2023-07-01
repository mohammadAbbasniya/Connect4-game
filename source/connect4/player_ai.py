from .player import Player
from .base_connect4 import Connect4
import math


class AIPlayer(Player):

    def get_move(self, game: 'Connect4', piece: 'int'):
        return minimax(game, piece, 5, -math.inf, math.inf, True)[0]


def minimax(game: 'Connect4', ai_piece, depth, alpha, beta, is_max):
    op_piece = game.opposite_piece(ai_piece)

    if game.is_terminal_node():
        if game.winning_move(ai_piece):
            return None, 10000
        elif game.winning_move(op_piece):
            return None, -10000
        else:
            return None, 0
    elif depth == 0:
        return None, evaluation(game, ai_piece)

    column = 0
    if is_max:
        value = -math.inf
        for i in game.get_valid_locations():
            child = game.copy()
            child.drop_piece(i, ai_piece)
            res = minimax(child, ai_piece, depth - 1, alpha, beta, False)[1]

            if child.winning_move(ai_piece):
                return i, 100000

            if value < res:
                value = res
                column = i
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:
        value = math.inf
        for i in game.get_valid_locations():
            child = game.copy()
            child.drop_piece(i, op_piece)
            res = minimax(child, ai_piece, depth - 1, alpha, beta, True)[1]
            if value > res:
                value = res
                column = i
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


def evaluate_window(window, piece, op_piece):
    score = 0

    if window.count(piece) == 4:
        score = 1000
    elif window.count(piece) == 3 and window.count(0) == 1:
        score = 35
    elif window.count(piece) == 2 and window.count(0) == 2:
        score = 10

    if window.count(op_piece) == 4:
        score = -1000
    elif window.count(op_piece) == 3 and window.count(0) == 1:
        score = -30
    elif window.count(op_piece) == 2 and window.count(0) == 2:
        score = -15

    return score


def evaluation(game: 'Connect4', piece):
    score = 0
    op_piece = game.opposite_piece(piece)

    # Score center column
    center_array = [int(i) for i in list(game.board[:, game.column_count // 2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    # Score Horizontal
    for r in range(game.row_count):
        row_array = [int(i) for i in list(game.board[r, :])]
        for c in range(game.column_count - 3):
            window = row_array[c:c + 4]
            score += evaluate_window(window, piece, op_piece)

    # Score Vertical
    for c in range(game.column_count):
        col_array = [int(i) for i in list(game.board[:, c])]
        for r in range(game.row_count - 3):
            window = col_array[r:r + 4]
            score += evaluate_window(window, piece, op_piece)

    # Score positive sloped diagonal
    for r in range(game.row_count - 3):
        for c in range(game.column_count - 3):
            window = [game.board[r + i][c + i] for i in range(4)]
            score += evaluate_window(window, piece, op_piece)

    # Score negative sloped diagonal
    for r in range(game.row_count - 3):
        for c in range(game.column_count - 3):
            window = [game.board[r + 3 - i][c + i] for i in range(4)]
            score += evaluate_window(window, piece, op_piece)

    return score
