import pygame


# Player Input Section
def process_input(paddle):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:  # Paddle moves left
        paddle.move_left()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Paddle moves right
        paddle.move_right()
