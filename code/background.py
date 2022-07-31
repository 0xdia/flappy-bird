import pygame


class Background:
    def __init__(self):
        self.images = [
            pygame.transform.scale2x(
                pygame.image.load("sprites/background-day.png").convert()
            ),
            pygame.transform.scale2x(
                pygame.image.load("sprites/background-night.png").convert()
            ),
        ]

    def draw(self, screen):
        screen.blit(self.images[1], (0, 0))
