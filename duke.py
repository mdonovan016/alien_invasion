import pygame

class TheDuke:
    """A class to manage Duke Nukem."""

    def __init__(self, ai_game) -> None:
        """Initializes the ship and sets its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/duke_nukem.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center ofthe screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) 