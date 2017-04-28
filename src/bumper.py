from base_rect import BaseRect
import pygame


class Bumper(BaseRect):
    
    def __init__(self, screen, y_pos, key_left, key_right):
        super(Bumper, self).__init__(screen, (100, y_pos), (50,10))
        self.bumper_dir = 0
        self.key_left = key_left
        self.key_right = key_right

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[self.key_right]:
            self.bumper_dir = 2
        if keys[self.key_left]:
            self.bumper_dir = -2

        if self.pos[0] + self.bumper_dir > 30 and self.pos[0] + self.bumper_dir + 50 < 310:
            self.pos[0] += self.bumper_dir
        self.bumper_dir  = 0

        