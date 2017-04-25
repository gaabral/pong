'''
Created on 24.04.2017

@author: Kamil
'''

import numpy
import math

class CollisionEngine(object):
    
    def __init__(self):
        self.entity_list = []
    
    def register_entity(self, entity):
        self.entity_list.append(entity)
        

    def update(self):
        for idx1 in range(0, len(self.entity_list)-1):
            for idx2 in range(idx1+1, len(self.entity_list)):
                self.check_collision(self.entity_list[idx1], self.entity_list[idx2])
            
    def check_collision(self, entity1, entity2):
        if entity1.__class__.__name__ == 'Ball' and entity2.__class__.__name__ == 'Bumper':
            self.check_collision_circle_rect(entity1, entity2, (entity1.ball_pos[0], entity1.ball_pos[1], 30), (entity2.x_pos, entity2.bumper_pos, 10, 50))
        
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
            return True
        return False