import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # pygame.image.load("sprites/yellowbird-midflap.png").convert_alpha()
        self.images = [
            pygame.transform.scale2x(
                pygame.image.load("sprites/yellowbird-downflap.png").convert_alpha()
            ),
            pygame.transform.scale2x(
                pygame.image.load("sprites/yellowbird-midflap.png").convert_alpha()
            ),
            pygame.transform.scale2x(
                pygame.image.load("sprites/yellowbird-upflap.png").convert_alpha()
            ),
        ]
        self.index = 0
        self.counter = 0
        self.flap_cooldown = 6
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = 0
        self.acceleration = 0.25
        self.started = False
        self.flapped = False
        # self.collided = False
        self.falling = False

    def start(self):
        self.started = True

    def bird_out(self, groundy):
        return groundy <= self.rect.bottom or self.rect.bottom <= 0

    def fall(self, groundy):
        if not self.falling:
            self.image = pygame.transform.rotate(self.images[self.index], -90)
            self.falling = True

        self.velocity += self.acceleration
        if self.rect.bottom < groundy:
            self.rect.y = min(self.rect.y + self.velocity, groundy)

    def update(self, groundy, collided):
        if not self.started:
            self.image = pygame.transform.rotate(self.images[self.index], 0)
            return

        if self.bird_out(groundy):
            return
        if collided:
            self.fall(groundy)
            return

        self.counter += 1
        if self.counter > self.flap_cooldown:
            self.counter = 0
            self.index = (self.index + 1) % len(self.images)

        self.velocity += self.acceleration
        if self.rect.bottom < groundy:
            self.rect.y = min(self.rect.y + self.velocity, groundy)

        if pygame.mouse.get_pressed()[0] == 1 and not self.flapped:
            if self.velocity >= 0:
                self.flapped == True
                self.velocity -= 7

        if pygame.mouse.get_pressed()[0] == 0:
            self.flapped = False

        self.image = pygame.transform.rotate(
            self.images[self.index], -2.5 * self.velocity
        )
