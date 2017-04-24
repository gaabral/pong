'''
Created on 24.04.2017

@author: Kamil
'''

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
            if self.check_collision_circle_segment((entity1.ball_pos[0], entity1.ball_pos[1], 30), (entity2.x_pos, entity2.bumper_pos, 50)):
                entity1.on_collision() 
        
    def check_collision_circle_segment(self, circle, segment):
        if circle[1] > segment[1] and circle[1] < segment[1] + segment[2] and abs(circle[0] - segment[0]) < circle[2]:
            return True
        return False