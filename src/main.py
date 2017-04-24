'''
Created on 22.04.2017

@author: Kamil
'''

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (600,200)
import pygame, sys
import ball
import bumper
import numpy
import collision_engine

if __name__ == '__main__':
    size = width, height = 320, 240
    screen = pygame.display.set_mode(size)

    coll_engine = collision_engine.CollisionEngine()

    ball = ball.Ball(screen)
    bumper1 = bumper.Bumper(screen, 300, pygame.K_UP, pygame.K_DOWN)
    #bumper2 = bumper.Bumper(screen, 300, pygame.K_w, pygame.K_s)

    coll_engine.register_entity(ball)
    coll_engine.register_entity(bumper1)
    #coll_engine.register_entity(bumper2)

    clk = pygame.time.Clock()
    
    
    a = [1,2,3]
    b = [2,3,4]
    print numpy.dot(a,b)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
    
        screen.fill((0,0,0))
        
        coll_engine.update()
        
        ball.update()
        ball.draw()
        bumper1.update()
        #bumper2.update()
        bumper1.draw()
        #bumper2.draw()

        pygame.display.flip()
        clk.tick(60)