'''
Created on 26.04.2017

@author: Kamil
'''
import pygame
from game_obj import GameObj

class BaseRect(GameObj):
    
    def __init__(self, screen, pos, size):
        super(BaseRect, self).__init__(screen)
        self.pos = list(pos)
        self.size = size
        
    def update(self):
        pass
    
    def on_collision(self):
        pass

    def draw(self):
        width, height = self.screen.get_size()
        pygame.draw.rect(self.screen, (255, 0, 255), (self.pos[0], height-self.size[1]-self.pos[1], self.size[0], self.size[1]))