import pygame


# Brick Section
class Brick:
    def __init__(self, position, width, height, color=(200, 0, 0)):
        self.position = position
        self.width = width
        self.height = height
        self.alive = True  # Brick state
        self.color = color

    # Display brick if not dead
    def draw(self, surface):
        if self.alive:
            pygame.draw.rect(surface, self.color, (*self.position, self.width, self.height))
