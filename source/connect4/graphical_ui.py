import pygame
from .base_connect4 import Connect4
from .player import Player
from .player_human_graphical import GraphicalHumanPlayer
from .player_ai import AIPlayer


class GraphicalUI:
    def __init__(self, options: 'GUIOptions', player1: 'Player', player2: 'Player'):
        self.opt = options
        self.game = Connect4(row_count=self.opt.rows, column_count=self.opt.cols)
        pygame.init()

        self.player1 = player1
        if player1.__class__ is GraphicalHumanPlayer:
            player1.gui_options = self.opt

        self.player2 = player2
        if player2.__class__ is GraphicalHumanPlayer:
            player2.gui_options = self.opt

    def draw_board(self):
        pygame.draw.rect(self.opt.surface, self.opt.backend_color,
                         (0, 0, self.opt.width, self.opt.square_size))

        for c in range(self.opt.cols):
            for r in range(self.opt.rows):
                pygame.draw.rect(self.opt.surface, self.opt.board_color, (c * self.opt.square_size, r * self.opt.square_size + self.opt.square_size, self.opt.square_size, self.opt.square_size))
                pygame.draw.circle(self.opt.surface, self.opt.boarder_color, (int(c * self.opt.square_size + self.opt.square_size / 2),
                                                                              int(r * self.opt.square_size + self.opt.square_size + self.opt.square_size / 2)), self.opt.radius + 2)
                pygame.draw.circle(self.opt.surface, self.opt.backend_color, (int(c * self.opt.square_size + self.opt.square_size / 2),
                                                                              int(r * self.opt.square_size + self.opt.square_size + self.opt.square_size / 2)), self.opt.radius)

        for c in range(self.opt.cols):
            for r in range(self.opt.rows):
                if self.game.board[r][c] == 1:
                    pygame.draw.circle(self.opt.surface, self.opt.player1_color, (
                        int(c * self.opt.square_size + self.opt.square_size / 2), self.opt.height - int(r * self.opt.square_size + self.opt.square_size / 2)), self.opt.radius)
                elif self.game.board[r][c] == 2:
                    pygame.draw.circle(self.opt.surface, self.opt.player2_color, (
                        int(c * self.opt.square_size + self.opt.square_size / 2), self.opt.height - int(r * self.opt.square_size + self.opt.square_size / 2)), self.opt.radius)
        pygame.display.update()

    def set_header(self, text, color=(0, 0, 0), size=75):
        font = pygame.font.SysFont("monospace", size)
        label = font.render(text, True, color)
        self.opt.surface.blit(label, (40, 10))
        pygame.display.update()

    def start(self):
        self.draw_board()
        pygame.display.update()
        turn_flag = True

        while True:
            if turn_flag:  # player 1
                if self.player1.__class__ is AIPlayer:
                    self.set_header("AI is thinking...", size=50)

                col = self.player1.get_move(self.game, 1)
                if col == -1:
                    pygame.quit()
                    return

                self.game.drop_piece(col, 1)
                self.draw_board()
                if self.game.winning_move(1):
                    self.set_header("Player 1 WON !!!", color=self.opt.player1_color)
                    break

            else:  # player 2
                if self.player2.__class__ is AIPlayer:
                    self.set_header("AI is thinking...")

                col = self.player2.get_move(self.game, 2)
                if col == -1:
                    pygame.quit()
                    return

                self.game.drop_piece(col, 2)
                self.draw_board()
                if self.game.winning_move(2):
                    self.set_header("Player 2 WON !!!", color=self.opt.player2_color)
                    break

            turn_flag = not turn_flag

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                pygame.display.update()


class GUIOptions:
    def __init__(self,
                 rows,
                 cols,
                 square_size=100,
                 radius=45,
                 board_color=(159, 143, 98),
                 backend_color=(207, 216, 220),
                 boarder_color=(0, 0, 0),
                 player1_color=(255, 0, 0),
                 player2_color=(255, 255, 0)):
        assert rows > 0, "number of rows must be grater than zero"
        assert cols > 0, "number of columns must be grater than zero"
        self.rows = rows
        self.cols = cols
        self.square_size = square_size
        self.radius = radius
        self.board_color = board_color
        self.backend_color = backend_color
        self.boarder_color = boarder_color
        self.player1_color = player1_color
        self.player2_color = player2_color

        self.width = self.cols * square_size
        self.height = (self.rows + 1) * square_size
        self.size = (self.width, self.height)
        self.surface = pygame.display.set_mode(self.size)

    def get_piece_color(self, piece):
        if piece == 1:
            return self.player1_color
        elif piece == 2:
            return self.player2_color
