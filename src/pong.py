'''
Created on 25.04.2017

@author: Kamil
'''
import pygame
import ball
import bumper
import collision_engine

class Pong(object):

    def __init__(self, screen):
        self.coll_engine = collision_engine.CollisionEngine()
        
        self.ball1 = ball.Ball(screen)
        self.coll_engine.register_entity(self.ball1)
        self.bumper1 = bumper.Bumper(screen, 150, pygame.K_UP, pygame.K_DOWN)
        self.coll_engine.register_entity(self.bumper1)
    
    def update(self):
        self.coll_engine.update()
        
        self.ball1.update()
        self.bumper1.update()
    
    def render(self):
        self.ball1.draw()
        self.bumper1.draw()
        
        
