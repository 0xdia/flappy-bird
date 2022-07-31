import pygame
import sys
import random
from .bird import Bird
from .ground import Ground
from .background import Background
from .pipe import Pipe


class Environment:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fps = 100

        self.screen_width = 567
        self.screen_height = 1024
        self.window_title = "Flappy Bird"
        self.scroll_speed = 2
        self.pipe_gap = 200
        self.pipe_frequency = 2000  # ms
        self.last_pipe_timestamp = pygame.time.get_ticks()

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.background = Background()

        self.ground = Ground(self.screen_height, self.scroll_speed)
        self.bird = Bird(200, int(self.ground.groundy / 2))
        self.bird_group = pygame.sprite.Group(self.bird)
        self.bird_group.add()

        self.pipe_group = pygame.sprite.Group()

        self.game_over = False

    def create_pipe_pair(self):
        pipe_height = random.randint(-175, 175)
        self.pipe_group.add(
            Pipe(
                self.screen_width,
                int(self.screen_height / 2 + pipe_height) + int(self.pipe_gap / 2),
                -1,
                self.scroll_speed,
            ),
            Pipe(
                self.screen_width,
                int(self.screen_height / 2 + pipe_height) - int(self.pipe_gap / 2),
                1,
                self.scroll_speed,
            ),
        )

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and not self.bird.started:
                    self.bird.start()

            self.clock.tick(self.fps)
            self.background.draw(self.screen)

            time_now = pygame.time.get_ticks()
            if time_now - self.last_pipe_timestamp > self.pipe_frequency:
                self.create_pipe_pair()
                self.last_pipe_timestamp = time_now
            self.pipe_group.draw(self.screen)
            

            self.bird_group.draw(self.screen)
            
            self.game_over = self.bird.bird_out(
                self.ground.groundy
            ) or pygame.sprite.groupcollide(
                self.bird_group, self.pipe_group, False, False
            )
            self.pipe_group.update(not self.game_over and self.bird.started)
            self.bird_group.update(self.ground.groundy, collided=self.game_over)
            self.ground.draw(
                self.screen, self.screen_width, not self.game_over and self.bird.started
            )

            pygame.display.update()
