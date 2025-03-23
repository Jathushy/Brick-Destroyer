import pygame


# Rendering Objects Section
def render(screen, paddle, ball, bricks):
    screen.fill((0, 0, 0))
    paddle.draw(screen)  # Drawing the paddle
    ball.draw(screen)  # Drawing the ball
    for brick in bricks:
        brick.draw(screen)  # Drawing the bricks
    pygame.display.flip()  # Display update
