from connect4 import *

# if __name__ == '__main__':
#     p1 = ConsoleHumanPlayer()
#     p2 = AIPlayer()
#     gui_game = ConsoleUI(6, 7, p1, p2)
#     gui_game.start()

if __name__ == '__main__':
    opts = GUIOptions(6, 7)
    p1 = GraphicalHumanPlayer()
    p2 = AIPlayer()
    gui_game = GraphicalUI(opts, p1, p2)
    gui_game.start()