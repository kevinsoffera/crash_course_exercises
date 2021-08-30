import pygame

class Broccoli:
    """A class to manage the broc."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('broccoli.png')
        self.rect = self.image.get_rect()

        # Start each broccoli at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the broc at its current location."""
        self.screen.blit(self.image, self.rect)

        