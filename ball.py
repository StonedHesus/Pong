import pygame
from pygame.sprite import Sprite

from random import randint

class Ball():
    """
    This here class manages the behavior of the ball game objects, whose scope is to bounce when hitting either one of
    the rackets(paddles) or the upper and bottom walls of the field.

    """
    def __init__(self, pong):
        super().__init__()
        self.screen = pong.screen
        self.screen_rect = pong.screen.get_rect()
        self.settings    = pong.settings
        self.color       = pong.settings.ball_color

        # Create the ball object in the middle of screen
        self.rect = pygame.Rect(600 - self.settings.ball_width, 400 - self.settings.ball_height,
                                self.settings.ball_width, self.settings.ball_height)

        # Store the decimal value for the ball's vertical and horizontal positions.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def move_on_x_axis(self):
        self.x += self.settings.ball_speed

        # Update the rect's x position.
        self.rect.x = self.x

    def move_on_y_axis(self):
        self.y += self.settings.ball_speed

        # Update the rect's y position.
        self.rect.y = self.y

    def randomly_pick_the_starting_direction(self):
        """
        Return two values, which represent the direction that we will use, determined by the axis(lines of the ball),
        in which the initial movement is bound to be heading.
        """
        # Zero represents the left bottom corner, one the right bottom one, two the top right one and three
        # the upper left one.
        random_corner = randint(0, 4)

        if random_corner == 0:
            return "bottom-left"
        elif random_corner == 1:
            return "bottom-right"
        elif random_corner == 2:
            return "top-right"
        elif random_corner == 3:
            return "top-left"


    def draw_ball(self):
        """Draw the ball to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)