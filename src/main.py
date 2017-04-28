'''
Created on 22.04.2017

@author: Kamil
'''

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (600,200)
import pygame, sys
import pong

if __name__ == '__main__':
    size = width, height = 720, 480
    screen = pygame.display.set_mode(size)
    
    clk = pygame.time.Clock()
    pong_game = pong.Pong(screen)
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
    
        screen.fill((0,0,0))
        
        pong_game.update()
        pong_game.render()

        pygame.display.flip()
        clk.tick(120)