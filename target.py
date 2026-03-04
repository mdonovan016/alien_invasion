import pygame
from pygame.sprite import Sprite


class Target(Sprite):

    """A class to manage the target."""

    def __init__(self, ai_game):
        """Initialize the target class."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.color = ai_game.settings.target_color
        self.rect = pygame.Rect(0, 0, self.settings.target_width, self.settings.target_height)
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)


    def check_edges(self):
        """Return True if target is at the top or bottom of the screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.top <= 0) or (self.rect.bottom >= screen_rect.bottom)

    def update_target_location(self):
        self.y += self.settings.target_speed * self.settings.target_direction
        self.rect.y = int(self.y)

    def draw_target(self):
        pygame.draw.rect(self.screen, self.color, self.rect)