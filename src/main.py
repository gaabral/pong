'''
Created on 22.04.2017

@author: Kamil
'''

import pygame, sys
import ball
import bumper
if __name__ == '__main__':
    size = width, height = 320, 240
    screen = pygame.display.set_mode(size)

    ball = ball.Ball(screen)
    bumper1 = bumper.Bumper(screen, 10, pygame.K_UP, pygame.K_DOWN)
    bumper2 = bumper.Bumper(screen, 300, pygame.K_w, pygame.K_s)

    clk = pygame.time.Clock()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
    
        screen.fill((0,0,0))
        ball.update()
        ball.draw()
        bumper1.update()
        bumper2.update()
        bumper1.draw()
        bumper2.draw()

        pygame.display.flip()
        clk.tick()
        print clk.get_fps()