'''
Created on 28.04.2017

@author: Kamil
'''

from base_rect import BaseRect

class Point(BaseRect):

    def __init__(self, screen, pong, x_pos, y_pos):
        super(Point, self).__init__(screen, (x_pos, y_pos), (10,10))
        self.pong = pong
        
    def on_collision(self):
        self.destroy()
        
    def destroy(self):
        self.pong.entity_list.remove(self)

        