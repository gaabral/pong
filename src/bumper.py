from game_obj import GameObj
import pygame


class Bumper(GameObj):
    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 255), (10, int(self.bumper_pos), 10, 50))
    def __init__(self, screen):
        super(Bumper, self).__init__(screen)
        self.bumper_pos = 10
        self.bumper_dir = 0

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.bumper_dir = -0.01
        if keys[pygame.K_DOWN]:
            self.bumper_dir = 0.01

        self.bumper_pos += self.bumper_dir
        self.bumper_dir  = 0
