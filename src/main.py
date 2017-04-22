'''
Created on 22.04.2017

@author: Kamil
'''

import pygame, sys

if __name__ == '__main__':
    size = width, height = 320, 240
    screen = pygame.display.set_mode(size)
    
    ball_pos = (100,100)
        
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
    
        screen.fill((0,0,0))
        pygame.draw.circle(screen, (255,0,0), ball_pos, 30, 10)
    
        pygame.display.flip()