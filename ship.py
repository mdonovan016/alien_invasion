import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game) -> None:
        """Initializes the ship and sets its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the left center ofthe screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a float for the ship's exact horizontal position. Pixels are only assigned as integers so we need something to store floats.
        self.y = float(self.rect.y)

        # Movement flags; starts with a ship that's not moving.
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's 'y' value, not the rect.
        if self.moving_up and 0 < self.rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
            
        # Update the rect object from self.y
        self.rect.y = self.y 

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) 