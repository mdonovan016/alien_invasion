class Settings:
    """A class to tore all settigns for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.ship_speed = 1.5 # Ship settings.
        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 30
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # fleet_direction of 1 represents right; -1 represents left.
        # Raindrop settings
        self.raindrop_speed = 3.0
        


        