import pygame


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position, scroll_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale2x(
            pygame.image.load("sprites/pipe-green.png").convert()
        )
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.scroll_speed = scroll_speed
        self.position = position
        if self.position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y]
        if position == -1:
            self.rect.topleft = [x, y]

    def update(self, keep_scrolling):
        if not keep_scrolling:
            return
        self.rect.x -= self.scroll_speed
        if self.rect.right < 0:
            self.kill()
