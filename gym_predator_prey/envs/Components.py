import numpy as np 
import copy 
class ObjectBase():
    def __init__(self, pos_x, pos_y, xmax, ymax):
        self.pos = (pos_x, pos_y)
        self.xmax = xmax 
        self.ymax = ymax 

    def set_pos(self, x,y):
        x = min(max(x, 0), self.xmax)
        y = min(max(y, 0), self.ymax)
        self.pos = (x,y)

    def get_pos(self):
        return self.pos


    def get_integer_pos(self):
        cur_pos = self.get_pos()
        return (int(np.round(cur_pos[0])), int(np.round(cur_pos[1])))


    def collision(self, other):
        raise NotImplementedError()


class PredatorBase(ObjectBase):
    def __init__(self, pos_x, pos_y, xmax, ymax, range):        
        super().__init__(pos_x, pos_y,  xmax, ymax)
        self.current_hp = 1
        self.range = range
        self.eaten = 0 
        self.eaten_positions = []

    def take_action(self, action):
        raise NotImplementedError()
    
    def become_hungry(self):
        self.eaten = 0 

    def increase_eaten_by_1(self):
        self.eaten += 1
    
    def is_satisfied(self):
        return True if self.eaten > 0 else False 

    def save_prey_pos(self, prey_pos):
        self.eaten_positions.append((copy.deepcopy(self.get_pos()), copy.deepcopy(prey_pos)))



class PreyBase(ObjectBase):
    def __init__(self, pos_x, pos_y, xmax, ymax):        
        super().__init__(pos_x, pos_y,  xmax, ymax)
        self.current_hp = 1

    def take_action(self, action):
        raise NotImplementedError()

    def reduce_hp_by_1(self):
        self.current_hp -= self.current_hp


    def is_alive(self):
        return True if self.current_hp >0 else False 


class MapBase():
    def __init__(self, width, height):
        self.width = width 
        self.height = height 


