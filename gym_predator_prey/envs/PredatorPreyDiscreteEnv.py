import gym 
from gym_predator_prey.envs.PredatorPreyBaseEnv import (
    PredatorPreyBaseEnv,
    PredatorBase,
    PreyBase,
    MapBase
)

class Prey(PreyBase):
    def __init__(self, pos_x, pos_y, max_hp, speed):
        super().__init__(pos_x, pos_y, max_hp, speed)
        self.action_space = gym.spaces.Discrete(5)
        self.observation_space = gym.spaces.Discrete()

    def take_action(self, action):
        return super().take_action(action)
    
    def get_obs(self, map):
        return super().get_obs(map)


class Predator(PredatorBase):
    def __init__(self, pos_x, pos_y, max_hp, speed):
        super().__init__(pos_x, pos_y, max_hp, speed)

    def take_action(self, action):
        return super().take_action(action)
    
    def get_obs(self, map):
        return super().get_obs(map)

class Map(MapBase):
    def __init__(self, width, height):
        super().__init__(width, height)

    


class PredatorPreyDiscreteEnv(PredatorPreyBaseEnv):
    def __init__(self, config:dict):
        self.config = config 
        
        super().__init__(
            
        )

