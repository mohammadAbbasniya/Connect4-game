import pygame
from .player import Player
from .base_connect4 import Connect4
import math


class GraphicalHumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.gui_options = None

    def get_move(self, game: 'Connect4', piece: 'int'):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.gui_options.surface, self.gui_options.backend_color,
                                     (0, 0, self.gui_options.width, self.gui_options.square_size))
                    posx = event.pos[0]
                    pygame.draw.circle(self.gui_options.surface, self.gui_options.get_piece_color(piece),
                                       (posx, int(self.gui_options.square_size / 2)), self.gui_options.radius)

                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.gui_options.surface, self.gui_options.backend_color,
                                     (0, 0, self.gui_options.width, self.gui_options.square_size))

                    posx = event.pos[0]
                    col = int(math.floor(posx / self.gui_options.square_size))

                    if game.is_valid_location(col):
                        return col
