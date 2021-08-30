import sys

import pygame

# 12.1 Blue Sky

class NewGame:
    """Overall class to manage assets and behavior."""

    def __init__(self):
        """Initialize game and set resources."""
        pygame.init()
        self.screen = pygame.display.set_mode(1200, 800)
        self.bg_color = (80, 230, 80)

        self.screen.fill(self.settings.bg_color)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = NewGame()
    ai.run_game()