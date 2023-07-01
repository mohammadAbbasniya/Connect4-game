from abc import ABC, abstractmethod
from .base_connect4 import Connect4


class Player(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_move(self, game: 'Connect4', piece: 'int'):
        pass
