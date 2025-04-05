import pygame
from models.paddle import Paddle
from models.ball import Ball
from models.brick import Brick
from models.collision import check_collision
from input_handler import process_input
from renderer import render


# Generating a grid of bricks
def create_brick_wall(rows, cols, brick_width, brick_height, padding, offset_x, offset_y):
    return [
        Brick([
            offset_x + col * (brick_width + padding) + (brick_width // 2 if row % 2 else 0),
            offset_y + row * (brick_height + padding)
        ], brick_width, brick_height)
        for row in range(rows) for col in range(cols)
    ]


# Main game loop
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Brick Destroyer")
    clock = pygame.time.Clock()

    paddle = Paddle([400, 570], 100, 10)  # Player's paddle
    ball = Ball([400, 300], 10, 5)  # The ball
    bricks = create_brick_wall(5, 10, 60, 20, 5, 50, 50)  # Create a wall of bricks

    score = 0  # Initialize score
    font = pygame.font.Font(None, 36)  # Font for displaying score

    running = True
    while running:
        for event in pygame.event.get():  # Check if user quits
            if event.type == pygame.QUIT:
                running = False
        process_input(paddle)  # Handle paddle movement
        ball.move()  # Move the ball
        score += check_collision(ball, paddle, bricks)  # Update score
        render(screen, paddle, ball, bricks, score, font)  # Displays everything
        clock.tick(60)


if __name__ == "__main__":
    main()
