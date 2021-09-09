import pygame
from pygame.sprite import Sprite

class Paddle():
    """The class that manages the behaviour of the paddle object, similar to a racket, that the users controls."""
    def __init__(self, pong):
        super().__init__()
        self.screen = pong.screen
        self.screen_rect = pong.screen.get_rect()
        self.settings = pong.settings
        self.color = pong.settings.paddle_color

        # Create a paddle rect at (0, 272) and then set the correct position, an operation which is done inside
        # the main game file, that being pong.py.
        self.rect = pygame.Rect(0, self.settings.screen_height/2 - self.settings.paddle_height,
                                self.settings.paddle_width, self.settings.paddle_height)

        # Store the decimal value for the paddle's vertical position.
        self.y = float(self.rect.y)

        # Moving flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the paddle's position based on the moving flags."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.paddle_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.paddle_speed

        # Update the rect object using the floating value stored in the y attribute.
        self.rect.y = self.y

    def draw_paddle(self):
        """Draw the paddle to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)