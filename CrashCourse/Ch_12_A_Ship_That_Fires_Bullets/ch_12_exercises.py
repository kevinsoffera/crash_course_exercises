import sys

import pygame

from broc import Broccoli
# 12.1 Blue Sky

class TestGame:
    """Overall class to manage assets and behavior."""

    def __init__(self):
        """Initialize game and set resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Test Game")\
        
        # Set the background color.
        self.bg_color = (100, 110, 255)

        self.broc = Broccoli(self)

    def run_game(self):
        """Start main loop for game."""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screem during each pass through the loop.
            self.screen.fill(self.bg_color)
            self.broc.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = TestGame()
    ai.run_game()