import pygame


def render(screen, paddle, ball, bricks, score, font, lives):
    screen.fill((0, 0, 0))
    paddle.draw(screen)     # Drawing the paddle
    ball.draw(screen)   # Drawing the ball
    for brick in bricks:
        brick.draw(screen)  # Drawing the bricks

    # Render score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Render lives
    lives_text = font.render("Lives: " + str(lives), True, (255, 255, 255))
    screen.blit(lives_text, (790 - lives_text.get_width(), 10))

    pygame.display.flip()   # Display update
