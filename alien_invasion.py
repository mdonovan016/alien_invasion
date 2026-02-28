import sys  # Used to exit the game cleanly
from time import sleep
import pygame  # Game library for graphics, input, and window management

from settings import Settings # A class that stores all settings for one instance of an Alien Invasion object
from ship import Ship # A class that stores all information for one instance of a Ship inside the Alien Invasion object
from bullet import Bullet 
from alien import Alien
from game_stats import GameStats

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
        self.stats = GameStats(self)
        self.bullets = pygame.sprite.Group()
        # self.load_sound = pygame.mixer.music.load('backgroundmusic')
        self.sound = pygame.mixer.Sound("music/balls.mp3")
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        pygame.display.set_caption("Alien Invasion") # Puts a title on the display.

    def run_game(self):
        """Start the main loop fo the game."""
        while True:
            self._check_events() # Watch for keyboard and mouse events.
            self.ship.update() # Update the location of the ship
            self.bullets.update() # Update the count and location of bullets
            self._update_bullets()
            self._update_aliens()
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
         if event.key == pygame.K_UP:
            # Move the ship up
            self.ship.moving_up = True
         elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
         elif event.key == pygame.K_q:
             sys.exit()
         elif event.key == pygame.K_SPACE:
             self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Responds to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.sound.stop()
            self.sound.play()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet alien collisions"""
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)

        if not self.aliens:
            # Destroy existing bullets and create a new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _update_bullets(self):
        """Update position of bulelts and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)
                # print(len(self.bullets))
        
        self._check_bullet_alien_collisions()
    
    def _create_alien(self, x_position, y_position):
            """Create an alien and place it in the row."""
            new_alien = Alien(self)
            new_alien.y = y_position
            new_alien.rect.x = x_position
            new_alien.rect.y = y_position
            self.aliens.add(new_alien)
    
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep addin aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        current_x, current_y = alien.rect.x, alien.rect.y
        while current_x > (5 * alien_width):
            while current_y > ( 2 * alien_height):
                self._create_alien(current_x, current_y)
                current_y -= 2 * alien_height
            # Finished a row; reset x value and incremeent y value.
            current_x -= 2 * alien_width
            current_y = alien.rect.y

    def _change_fleet_direction(self):
        """Moves the entire fleet left and changes the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached the top or bottom."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        
        if self.stats.ships_left > 0:
            # Decrement the number of ships left
            self.stats.ships_left -= 1

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
        else: 
            self.game_active = False

        # Pause
        sleep(0.5)

    def _check_aliens_left_edge(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens:
            if alien.rect.left <= 0:
                # Get rid of any remaining bullets and aliens.
                self._ship_hit()
                break

    def _update_aliens(self):
        """Checks if the fleet is at an edge, then updates positions."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen
        self._check_aliens_left_edge()        
        
    def _update_screen(self):
         """Updated images on the screen, and flip to the new screen."""
         self.screen.fill(self.settings.bg_color) # Redraw the screen during each pass through the loop
         for bullet in self.bullets.sprites():
             bullet.draw_bullet()
         self.ship.blitme()
         self.aliens.draw(self.screen)
         pygame.display.flip() 


if __name__ == '__main__':  # Only runs if this file is executed directly, not imported

    # Make a game instance , and run the game.
    ai = AlienInvasion()  # calls __init__, sets up the window
    ai.run_game()          # starts the infinite game loop
