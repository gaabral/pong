from game_obj import GameObj
import pygame


class Bumper(GameObj):
    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 255), (self.x_pos, self.bumper_pos, 10, 50))
    def __init__(self, screen, x_pos, key_up, key_down):
        super(Bumper, self).__init__(screen)
        self.bumper_pos = 0
        self.bumper_dir = 0
        self.key_up = key_up
        self.key_down = key_down
        self.x_pos =x_pos

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[self.key_up]:
            self.bumper_dir = -2
        if keys[self.key_down]:
            self.bumper_dir = 2

        self.bumper_pos += self.bumper_dir
        self.bumper_dir  = 0
