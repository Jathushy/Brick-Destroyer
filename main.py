import pygame
import random
from models.paddle import Paddle
from models.ball import Ball
from models.brick import Brick
from models.collision import check_collision
from input_handler import process_input
from renderer import render

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)


# Font and size assignment
def get_font(font_type):
    if font_type == "title":
        return pygame.font.Font(None, 72)
    elif font_type == "text":
        return pygame.font.Font(None, 36)


# Generating a grid of bricks
def create_brick_wall(rows, cols, brick_width, brick_height, padding, offset_x, offset_y):
    return [
        Brick([
            offset_x + col * (brick_width + padding) + (brick_width // 2 if row % 2 else 0),
            offset_y + row * (brick_height + padding)
        ], brick_width, brick_height)
        for row in range(rows) for col in range(cols)
    ]


# Title screen
def show_title_screen(screen, clock):
    title_text = get_font("title").render("Brick Destroyer", True, white)
    text_1 = get_font("text").render("Press Enter to begin", True, white)
    text_2 = get_font("text").render("Use arrow keys or A/D to move the paddle", True, white)
    waiting = True

    while waiting:
        screen.fill(black)
        screen.blit(title_text, ((800 - title_text.get_width()) // 2, 200))
        screen.blit(text_1, ((800 - text_1.get_width()) // 2, 320))
        screen.blit(text_2, ((800 - text_2.get_width()) // 2, 370))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
        clock.tick(60)


# Game over screen
def show_game_over_screen(screen, clock, score):
    # Text
    title_text = get_font("title").render("Game Over", True, white)
    score_text = get_font("text").render("Your score: " + str(score), True, white)
    try_again_text = get_font("text").render("Try Again", True, black)
    exit_text = get_font("text").render("Exit", True, black)
    # Buttons
    try_again_rect = pygame.Rect(300, 350, 200, 50)
    exit_rect = pygame.Rect(300, 420, 200, 50)

    while True:
        screen.fill(black)
        screen.blit(title_text, ((800 - title_text.get_width()) // 2, 150))
        screen.blit(score_text, ((800 - score_text.get_width()) // 2, 250))
        pygame.draw.rect(screen, gray, try_again_rect)
        pygame.draw.rect(screen, gray, exit_rect)
        screen.blit(try_again_text, (340, 360))
        screen.blit(exit_text, (370, 430))
        pygame.display.flip()
        # Button click
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if try_again_rect.collidepoint(event.pos):
                    return True
                elif exit_rect.collidepoint(event.pos):
                    return False
        clock.tick(60)


# Main game loop
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Brick Destroyer")
    clock = pygame.time.Clock()

    while True:
        show_title_screen(screen, clock)  # Showing title page
        paddle = Paddle([400, 570], 100, 10)  # Player's paddle
        ball = Ball([random.randint(20, 780), random.randint(350, 500)], 10, 5)  # The ball
        bricks = create_brick_wall(5, 10, 60, 20, 5, 50, 50)  # Create a wall of bricks
        score = 0  # Initial value of score
        lives = 3  # Player starts with 3 lives
        running = True
        game_over = False

        while running:
            for event in pygame.event.get():  # Check if user quits
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()

            process_input(paddle)  # Handle paddle movement
            ball.move()  # Move the ball

            if ball.position[1] > 600:  # Ball falls below screen
                lives -= 1
                if lives == 0:
                    game_over = True
                    running = False
                else:
                    ball = Ball([random.randint(20, 780), random.randint(350, 500)], 10, 5)  # New ball

            score += check_collision(ball, paddle, bricks)  # Update score
            render(screen, paddle, ball, bricks, score, get_font("text"), lives)  # Displays everything
            clock.tick(60)

        if game_over:
            try_again = show_game_over_screen(screen, clock, score)
            if not try_again:
                break  # Exit game


if __name__ == "__main__":
    main()
