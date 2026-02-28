import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop in the grid."""

    def __init__(self, ai_game):
        """Initialize the raindrop and set its starting position."""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the raindrop image and set its rect attribute
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each raindrop at the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    
    def update(self):
        """Move rain down the screen."""
        self.rect. y += self.settings.raindrop_speed