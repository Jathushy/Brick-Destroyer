import pygame


def render(screen, paddle, ball, bricks, score, font):
    screen.fill((0, 0, 0))
    paddle.draw(screen)     # Drawing the paddle
    ball.draw(screen)   # Drawing the ball
    for brick in bricks:
        brick.draw(screen)  # Drawing the bricks

    # Render score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()   # Display update
