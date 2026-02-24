import sys  # Used to exit the game cleanly

import pygame  # Game library for graphics, input, and window management

from settings import Settings # A class that stores all settings for one instance of an Alien Invasion object

from ship import Ship
from bullet import Bullet
from duke import TheDuke

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock() # Creates a clock object for each game instance.
        self.settings = Settings() # Creats a Settings object for each game instance.
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # Creates and sets dimensions for the display.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.ship = Ship(self)
        self.duke = TheDuke(self)
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption("Alien Invasion") # Puts a title on the display.

    def run_game(self):
        """Start the main loop fo the game."""
        while True:
            self._check_events() # Watch for keyboard and mouse events.
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen() # Make the most recently drawn screen visible.
            self.clock.tick(60) # Ensures game will never render more thatn 60 FPS.

    def _check_events(self):
        """Responds to key presses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
         """Responds to key presses."""
         if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
         elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
         elif event.key == pygame.K_q:
             sys.exit()
         elif event.key == pygame.K_SPACE:
             self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Responds to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bulelts and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                # print(len(self.bullets))
        
        
    def _update_screen(self):
         """Updated images on the screen, and flip to the new screen."""
         self.screen.fill(self.settings.bg_color) # Redraw the screen during each pass through the loop
         for bullet in self.bullets.sprites():
             bullet.draw_bullet()
         self.ship.blitme()
         self.duke.blitme()
         pygame.display.flip() 


if __name__ == '__main__':  # Only runs if this file is executed directly, not imported

    # Make a game instance , and run the game.
    ai = AlienInvasion()  # calls __init__, sets up the window
    ai.run_game()          # starts the infinite game loop
