from game_obj import GameObj
import pygame


class Ball(GameObj):
    def draw(self):
        pygame.draw.circle(self.screen, (255,0,0), tuple(int(x) for x in self.ball_pos), 30, 10)

    def __init__(self, screen):
        super(Ball, self).__init__(screen)
        self.ball_pos = [100, 100]
        self.ball_dir = [1, 2]

    def update(self):
        self.ball_pos = list(sum(x) for x in zip(self.ball_pos, self.ball_dir))

        radius = 30
        
        if self.ball_pos[0]+radius > 320 or self.ball_pos[0]-radius < 0:
            #self.ball_pos = [160, 120]
            self.ball_dir[0] *=-1

        if self.ball_pos[1]+radius > 240 or self.ball_pos[1]-radius < 0:
            self.ball_dir[1] *=-1

    def on_collision(self):
        self.ball_dir[0] *=-1