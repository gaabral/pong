'''
Created on 24.04.2017

@author: Kamil
'''

import numpy
import math

class CollisionEngine(object):
    
    def __init__(self, entity_list):
        self.entity_list = entity_list
    
    def register_entity(self, entity):
        self.entity_list.append(entity)
        

    def update(self):
        it = iter(self.entity_list)

        ball = it.next()
        for rect in it:
            self.check_collision(ball, rect)
            
    def check_collision(self, entity1, entity2):
        if entity1.__class__.__name__ == 'Ball':
            self.check_collision_circle_rect(entity1, entity2, (entity1.ball_pos[0], entity1.ball_pos[1], entity1.ball_rad), (entity2.pos[0], entity2.pos[1], entity2.size[0], entity2.size[1]))
        
    def check_collision_circle_rect(self, entity1, entity2, circle, rect):

        x = max(rect[0], min(circle[0], rect[0]+rect[2]))
        y = max(rect[1], min(circle[1], rect[1]+rect[3]))

        x_dist = x - circle[0]
        y_dist = y - circle[1]
        col_vector = numpy.array([x_dist, y_dist])
        col_norm_vector = col_vector / numpy.linalg.norm(col_vector)
        
        if x_dist*x_dist + y_dist*y_dist <= circle[2]*circle[2]:
            projection_depth = circle[2]-math.sqrt(x_dist*x_dist + y_dist*y_dist)
            entity1.ball_pos += -projection_depth*col_norm_vector
            entity1.on_collision(col_norm_vector)
            entity2.on_collision()
            return True
        return False