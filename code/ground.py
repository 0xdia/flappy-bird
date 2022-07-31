import pygame


class Ground:
    def __init__(self, screen_height, scroll_speed):
        self.image = pygame.transform.scale2x(
            pygame.image.load("sprites/base.png").convert()
        )
        self.groundx = 0
        self.groundy = screen_height - self.image.get_height() + 50
        self.scroll_speed = scroll_speed

    def scroll(self, screen_width):
        self.groundx -= self.scroll_speed
        if self.groundx <= -screen_width:
            self.groundx = 0

    def draw(self, screen, screen_width, keep_scrolling):
        if keep_scrolling:
            self.scroll(screen_width)
        screen.blit(self.image, (self.groundx, self.groundy))
        screen.blit(self.image, (self.groundx + self.image.get_width(), self.groundy))
