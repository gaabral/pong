'''
Created on 22.04.2017

@author: Kamil
'''

import pygame, sys
import ball
if __name__ == '__main__':
    size = width, height = 320, 240
    screen = pygame.display.set_mode(size)

    ball = ball.Ball(screen)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
    
        screen.fill((0,0,0))
        ball.update()
        ball.draw()
        pygame.display.flip()