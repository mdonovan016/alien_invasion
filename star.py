import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single start in the sky."""

    def __init__(self, ai_game):
        """Initialize the star and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the star image and set its rect attribute
        self.image = pygame.image.load('images/star.bmp')
        self.image.set_alpha(100)  # 0 = invisible, 255 = fully visible
        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height