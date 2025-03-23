from models.paddle import Paddle
from models.ball import Ball
from models.collision import check_collision
# Testing Section


# Testing paddle movement
def test_paddle_movement():
    paddle = Paddle([400, 570], 100, 10)    # Creates paddle
    # Moves paddle left and right then checks if positions updates correctly
    paddle.move_left()
    assert paddle.position[0] == 390
    paddle.move_right()
    assert paddle.position[0] == 400

    # Testing to see if paddle moves beyond boundaries
    paddle.position[0] = 0
    paddle.move_left()
    assert paddle.position[0] == 0  # Left boundary
    paddle.position[0] = 700
    paddle.move_right()
    assert paddle.position[0] == 700  # Right boundary


# Testing ball movement
def test_ball_movement():
    ball = Ball([400, 300], 10, 5)  # Creates ball
    # Moves the ball and checks if it updates correctly
    ball.move()
    assert ball.position == [405, 295]

    # Change ball direction
    ball.direction = [-1, 1]
    ball.move()
    assert ball.position == [400, 300]  # Checks again to see if ball moved correctly


# Testing the ball's collision with walls
def test_ball_wall_collision():
    ball = Ball([5, 5], 10, 5)  # Creates another ball
    ball.direction = [-1, -1]
    ball.move() # Move the ball
    assert ball.direction == [1, 1]  # Should bounce off the wall

    # Place ball near the top-right corner
    ball.position = [795, 5]
    ball.move()
    assert ball.direction == [-1, 1]  # Ball should bounce off the right wall


# Testing ball collision with the paddle
def test_ball_paddle_collision():
    paddle = Paddle([350, 570], 100, 10)    # Create paddle
    ball = Ball([375, 560], 10, 5)  # Create ball
    check_collision(ball, paddle, [])   # Checks for ball and paddle collision
    assert ball.direction[1] == 1   # Sees if the ball bounces correctly
