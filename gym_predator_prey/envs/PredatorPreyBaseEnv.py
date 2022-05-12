
import gym 

class ObjectBase():
    def __init__(self, pos_x, pos_y):
        self.pos = (pos_x, pos_y)

    def collision(self, other):
        raise NotImplementedError()


class PredatorBase(ObjectBase):
    def __init__(self, pos_x, pos_y, max_hp, speed):        
        super().__init__(pos_x, pos_y)
        self.max_hp = max_hp
        self.speed = speed
        self.current_hp = max_hp 

    def take_action(self, action):
        raise NotImplementedError()

    def get_obs(self, map):
        raise NotImplementedError()

class PreyBase(ObjectBase):
    def __init__(self, pos_x, pos_y, max_hp, speed):        
        super().__init__(pos_x, pos_y)
        self.max_hp = max_hp
        self.speed = speed
        self.current_hp = max_hp 

    def take_action(self, action):
        raise NotImplementedError()

    def get_obs(self, map):
            raise NotImplementedError()

class MapBase():
    def __init__(self, width, height):
        self.width = width 
        self.height = height 


class PredatorPreyBaseEnv(gym.Env):
    def __init__(self, predator_configs, prey_configs, map_configs):
        self.n_predators = len(predator_configs)
        self.n_preys = len(prey_configs)



