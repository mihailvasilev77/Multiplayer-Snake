# Multiplayer snake
A version of the classic snake game with a second player twist. <br />
Python version: 3.8.6 <br />
Modules  used: pygame, random, sys 

# Running and Installation
`git clone https://github.com/mihailvasilev77/ProjectPy.git` <br />
`cd ProjectPy` <br />
`pip install -r requirements.txt` or `python -m pip install -r requirements.txt`<br />
`py main.py` or `python main.py`

# How does it work?
This version of the snake game provides an option for the classical singleplayer snake game and two multiplayer gamemodes.
The first gamemode is called Time Rush where the players main goal is to collect as much fruits as possible for the period of time.
The second gamemode is the vanilla style in which whoever crashes first, loses.

# Classes
* mains() - the class with the base for the two snakes
* Snake() - the first snake
* Snake1() - the second snake
* Food() - the food

# Functions
1. Snake, Snake1, mains
* **get_head_position()** - returns the value of the head position
* **turn()** - changes the direction of the snake
* **move()** - moving the snake in its direction, it also checks for self collision
* **reset()** - restores the snake to its default
* **draw()** - draws the snake onto the board
2. Food
* **randomize_position()** - generates a position for the food to spawn in
* **draw()** - draws the food onto the board
3. Other
* **drawBoard()** - draws the board in a checkers/chess pattern
* **handleMovement()** - checks for keyboard input and moves the coresponding snake
* **snakeCol()** - checks for collision with the other snake
* **eatCheck()** - checks if food has been consumed
* **gameloop()** - a infinitive while loop that runs the game
* **main()** - selects gamemodes and the functions used to start the game
