import pygame
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Ball Management Section
class Ball:
    def __init__(self, position, radius, speed):
        self.position = position
        self.radius = radius
        self.speed = speed
        self.direction = [1, -1]  # Starting direction

    # Move the ball
    def move(self):
        self.position[0] += self.speed * self.direction[0]
        self.position[1] += self.speed * self.direction[1]

        # Bounce off left and right walls
        if self.position[0] <= 0 or self.position[0] >= SCREEN_WIDTH:
            self.direction[0] *= -1
        # Bounce off the top wall
        if self.position[1] <= 0:
            self.direction[1] *= -1

    # Display the ball on screen
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius)
