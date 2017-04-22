'''
Created on 22.04.2017

@author: Kamil
'''

import pygame, sys

if __name__ == '__main__':
    size = width, height = 320, 240
    screen = pygame.display.set_mode(size)
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
    
        pygame.display.flip()