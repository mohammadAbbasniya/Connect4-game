# Full Option Connect4 Game With Python 🎮 🐍
This is a python package including an implementation of Connect 4 game with a medium-level artificial intelligence player developed using minimax algorithm (with **&alpha;&beta;** pruning). I’ve tried to separate different parts of the whole project into several classes in order to demonstrate the single responsibility principle.

## About Connect4
Connect Four (also known as Connect 4, Four Up, Plot Four, Find Four, Captain's Mistress, Four in a Row, Drop Four, and Gravitrips in the Soviet Union) is a two-player connection rack game, in which the players choose a color and then take turns dropping colored tokens into a six-row, seven-column vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own tokens. Connect Four is a solved game. The first player can always win by playing the right moves [[Wiki](https://en.wikipedia.org/wiki/Connect_Four)].

<p align="center">
  <img  src="https://github.com/mohammadAbbasniya/Connect4-game/blob/main/res/gameplaye.gif">
</p>

## About Project Files
Here is a simple description of each file of this project. 
### base_connect4.py
This file contains class `Connect4` which has all needed functionalities of a Connect 4 game. This class works **independently** from the user interface of the program. It means that this class only provides data and methods of a Connect 4 game, not what you see as output.
### player.py
This file contains `Player` class which is the parent class for each player class; because there are several players with different behaviors in this project, we need a parent class to organize these players. `Player` class is an abstract class and cannot be instantiated; only inheriting from it is possible. This class has an abstract method `get_move` which takes a `Connect4` object and a `piece` and must return the selected move by the player. 
### console_ui.py
This file contains `ConsoleUI` class which takes two players and the size of Connect 4 game in its constructor and runs the game step by step with a command line super simple interface like this:
<p align="center">
  <img height=450 src="https://github.com/mohammadAbbasniya/Connect4-game/blob/main/res/console-sample.png">
</p>

### graphical_ui.py
This file contains two classes, the `GraphicalUI` and `GUIOptions`. The GraphicalUI class takes two players and a GUIOptions object. The GraphicalUI (like `ConsoleUI`) runs the game step by step with a graphical user interface developed by `pygame`. The GUIOptions object contains the options of user interface (e.g., size of game, size of user interface, colors, etc.). 
<p align="center">
  <img height=450 src="https://github.com/mohammadAbbasniya/Connect4-game/blob/main/res/graphical-sample.png">
</p>

### player_human_console.py
This file contains `ConsoleHumanPlayer` class which is inherited from `Player` class and implemented its abstract method in order to behave like a human player who’s using a console interface.
### player_human_graphical.py
This file contains `GraphicalHumanPlayer` class which is inherited from `Player` class and implemented its abstract method in order to behave like a human player who’s using a graphical interface.
### player_ai.py
This file contains `AIPlayer` class which is inherited from `Player` class and implemented its abstract method in order to behave like an artificial intelligence player. This class doesn’t care about the user interface (graphical / console). The minimax algorithm is employed in this class to choose the best move for AIPlayer. The minimax algorithm only looks at five steps ahead and prunes the futile brunches using **&alpha;&beta;** pruning.


