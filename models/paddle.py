import pygame
SCREEN_WIDTH = 800


# Paddle Managing Section
class Paddle:
    def __init__(self, position, width, speed, height=15):
        self.position = position
        self.width = width
        self.height = height
        self.speed = speed

    # Makes sure the paddle doesn't go off the screen
    def move_left(self):
        self.position[0] = max(self.position[0] - self.speed, 0)

    def move_right(self):
        self.position[0] = min(self.position[0] + self.speed, SCREEN_WIDTH - self.width)

    # Displays the paddle
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (*self.position, self.width, self.height), border_radius=8)
