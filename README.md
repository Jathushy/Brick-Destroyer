# **Brick-Destroyer**
Didn't you read the name, the game is about destroying bricks! What more do you need?

## **Project Overview:**
Brick Destroyer is an arcade game built using Pygame. Control a paddle to bounce a ball upwards, aiming to 
destroy all the bricks on screen.

### Key Features:
**Brick Wall:** A grid of bricks that the player must destroy to win.

**Paddle Control:** Use arrow keys or A/D to move the paddle horizontally.

**Ball Physics:** A bouncing ball that interacts with walls, the paddle, and bricks.

**Collision Detection:** Collision handling between the ball, paddle, and bricks.

**Lives System:** Players have three lives; losing the ball too many times ends the game.

**Win and Game Over Screens:** Screens with score display and replay and exit options.

## **Setup Instructions:**
Python need to be installed with the PyGame module. To run the Brick Destroyer game run the "main.py" file.

## **Usage Guide:**
Games uses a/d and arrow keys for side to side movement. This is also mentioned within the game.

## **Requirements Reference:**
1. The game displays a title screen when launched using the show_title_screen() function in main.py, which presents 
the game title, instructions for controls, and waits for the player to press Enter to begin.


2. The player controls a paddle to bounce the ball back up, this is done by the Paddle class in paddle.py manages 
the paddle’s position, movement speed, and ensures it stays within the screen 
boundaries.


3. Bricks are generated using the create_brick_wall() function. Collision detection is performed by the 
check_collision() function, which changes the alive status of the bricks when hit and updates the score.


4. The game keeps track of the score and displays it by incrementing whenever a brick is destroyed and is rendered on 
the screen by the render() function in renderer.py.


5. The show_game_over_screen() function displays a "Game Over" message, the player's score, and provides options to try 
again or exit the game.


6. When the score reaches 50 which is the number blocks, the game ends and show_win_screen() displays a message and 
options.

## **Credits and Acknowledgements:**
- AI was used in this project to help set up a running layout for the bricks, collision detection and some bug fixing.