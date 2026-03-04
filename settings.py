class Settings:
    """A class to tore all settigns for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""

        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.ship_speed = 1.5 # Ship settings.

        # Ship settings
        self.ship_speed = 2
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 300
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 30
        self.bullet_misses = 0

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # Target settings
        self.target_width = 200
        self.target_height = 100
        self.target_color = (0, 0, 0)
        self.target_speed = 5
        self.target_direction = 1
        
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # fleet_direction of 1 represents right; -1 represents left.

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.target_speed *= self.speedup_scale

