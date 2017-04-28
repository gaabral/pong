from game_obj import GameObj
import pygame
import rendering_helper
import numpy
import math

class Ball(GameObj):
    def draw(self):
        pygame.draw.circle(self.screen, (255,0,0), tuple(int(x) for x in rendering_helper.recalc_position(self.screen, *self.ball_pos)), self.ball_rad, self.ball_rad)

    def __init__(self, screen):
        super(Ball, self).__init__(screen)
        self.ball_pos = [100, 100]
        self.ball_dir = [1, 2]
        self.ball_rad = 20

    def update(self):
        self.ball_pos = list(sum(x) for x in zip(self.ball_pos, self.ball_dir))

    def on_collision(self, col_norm_vector):
        if numpy.dot(col_norm_vector, self.ball_dir) > 0:
            dir_aux = numpy.array(self.ball_dir)
            new_dir = list(dir_aux - 2*numpy.dot(dir_aux, col_norm_vector)*col_norm_vector)
            if not math.isnan(new_dir[0]) and not math.isnan(new_dir[1]):
                self.ball_dir = new_dir
                