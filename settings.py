class Settings():
    """Manages the games settings and attributes."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (0, 0, 0)

        # Paddle settings
        self.paddle_width = 18
        self.paddle_height = 128
        self.paddle_color = (255, 255, 255)
        self.paddle_speed = 1.95

        # Ball settings
        self.ball_color = (255, 255, 255)
        self.ball_width = 28
        self.ball_height = 28
        self.ball_speed = 1.75