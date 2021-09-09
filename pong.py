import pygame
from settings import Settings
from paddle import Paddle
from ball import Ball

from os import sys

class Pong():
    """
    Main class for the Pong game. This here class is responsible for managing the game's functions, features and assets,
    but also for running and maintaining it, thru a series of helper functions and clear and conscience approaches.
    """

    def __init__(self):
        """Initialize the game, and creates assets and behaviour for it."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Pong")

        # Create the two player objects, by making two instances of the paddle class
        self.paddle_one = Paddle(self)
        self.paddle_two = Paddle(self)

        # Alter the coordinates a trifle, so as to have the second paddle displayed on the right of the screen,
        # with a paddle's width separating the object from the border, a distance that we apply to the right-side
        # element as well.
        self.paddle_two.rect.x = self.settings.screen_width - 2*self.settings.paddle_width
        self.paddle_one.rect.x += self.settings.paddle_width

        # Create the ball object.
        self.ball = Ball(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
           self._check_events()
           self.paddle_one.update()
           self.paddle_two.update()
           self._initial_ball_movement()
           self._update_screen()

    def _initial_ball_movement(self):
        """Set the ball moving at the beginning of the game."""
        # Get the direction in which the ball will be heading.
        direction = self.ball.randomly_pick_the_starting_direction()

        if direction == "bottom-left":
            self.ball.move_on_x_axis()
            self.ball.move_on_y_axis()
        elif direction == "bottom-right":
            self.ball.move_on_x_axis()
            self.ball.move_on_y_axis()
        elif direction == "top-left":
            self.ball.move_on_x_axis()
            self.ball.move_on_y_axis()
        elif direction == "top-right":
            self.ball.move_on_x_axis()
            self.ball.move_on_y_axis()



    def _check_events(self):
        """Listen for keyboard or mouse events and respond to them accordingly."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_w:
            self.paddle_one.moving_up = True
        elif event.key == pygame.K_s:
            self.paddle_one.moving_down = True
        elif event.key == pygame.K_UP:
            self.paddle_two.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.paddle_two.moving_down = True


    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_w:
            self.paddle_one.moving_up = False
        elif event.key == pygame.K_s:
            self.paddle_one.moving_down = False
        elif event.key == pygame.K_UP:
            self.paddle_two.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.paddle_two.moving_down = False

    def _update_screen(self):
        """Update the screen, based on the events that occur and flip it to the next frame."""
        self.screen.fill(self.settings.background_color)
        self.paddle_one.draw_paddle()
        self.paddle_two.draw_paddle()
        self.ball.draw_ball()


        pygame.display.flip()

if __name__ == '__main__':
    pong = Pong()
    pong.run_game()