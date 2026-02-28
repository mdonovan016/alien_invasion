import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and sets its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the bottom right of the screen.
        self.rect.x = self.settings.screen_width - self.rect.width
        self.rect.y = self.settings.screen_height - self.rect.height

        # Store the alien's exact horizontal position
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at the top or bottom of the screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.top <= 0) or (self.rect.bottom >= screen_rect.bottom)
    
    def update(self):
        # Move alien up or down. 
        self.y += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y