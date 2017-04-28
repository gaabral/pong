'''
Created on 25.04.2017

@author: Kamil
'''
import pygame
import ball
import bumper
import collision_engine
import base_rect
import point

class Pong(object):

    def __init__(self, screen):
        self.entity_list = []
        self.coll_engine = collision_engine.CollisionEngine(self.entity_list)
        
        self.ball1 = ball.Ball(screen)
        self.entity_list.append(self.ball1)
        self.bumper1 = bumper.Bumper(screen, 40, pygame.K_LEFT, pygame.K_RIGHT)
        self.entity_list.append(self.bumper1)
        
        wall = base_rect.BaseRect(screen, (20, 450), (300, 10))
        self.entity_list.append(wall)
        
        wall = base_rect.BaseRect(screen, (310, 10), (10, 440))
        self.entity_list.append(wall)
        
        wall = base_rect.BaseRect(screen, (20, 10), (300, 10))
        self.entity_list.append(wall)
        
        wall = base_rect.BaseRect(screen, (20, 10), (10, 440))
        self.entity_list.append(wall)
        
        for x in range(0, 250, 15):
            for y in range(0, 35, 15):
                point1 = point.Point(screen, self, 50+x, 300+y)
                self.entity_list.append(point1)
    
    def update(self):
        self.coll_engine.update()
        
        self.ball1.update()
        self.bumper1.update()
        
        for en in self.entity_list:
            en.update()
    
    def render(self):
        self.ball1.draw()
        self.bumper1.draw()

        for en in self.entity_list:
            en.draw()
