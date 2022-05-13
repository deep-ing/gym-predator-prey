import gym 
from gym_predator_prey.utils.renderer import TerminalRenderer
from gym_predator_prey.envs.Components import (
    PredatorBase,
    PreyBase,
    MapBase,
)
from gym_predator_prey.envs.BaseEnv import BaseEnv
import numpy as np 

dx = [0,-1,0,0,1]
dy = [0,0,1,-1,0]

class Prey(PreyBase):

    def __init__(self, pos_x, pos_y, xmax, ymax, max_speed):
        super().__init__(pos_x, pos_y, xmax, ymax)
        self.max_speed = max_speed
        self.action_space = gym.spaces.Dict({"direction":gym.spaces.Discrete(5), "speed": gym.spaces.Box(0, max_speed, (1,))})
        self.observation_space = gym.spaces.Box(-np.inf, np.inf, (3,))

    def take_action(self, action):
        direction = action["direction"]
        speed = min(action["speed"], self.max_speed)
        d = (dx[direction], dy[direction])
        cur_pos = self.get_pos()
        new_pos = (cur_pos[0] + d[0]*speed, cur_pos[1] + d[1]*speed)
        self.set_pos(*new_pos)
    
    def get_info(self):
        info = [self.pos[0], self.pos[1], self.max_speed]
        return info 

    def get_integer_pos(self):
        cur_pos = self.get_pos()
        return (int(cur_pos[0]), int(cur_pos[1]))

class Predator(PredatorBase):
    def __init__(self, pos_x, pos_y, xmax, ymax, range, max_speed):
        super().__init__(pos_x, pos_y, xmax, ymax, range)
        self.max_speed = max_speed
        self.action_space = gym.spaces.Dict({"direction":gym.spaces.Discrete(5), "speed": gym.spaces.Box(0, max_speed, (1,))})
        self.observation_space = gym.spaces.Box(-np.inf, np.inf, (3,))

    def take_action(self, action):
        direction = action["direction"]
        speed = min(action["speed"], self.max_speed)
        d = (dx[direction], dy[direction])
        cur_pos = self.get_pos()
        new_pos = (cur_pos[0] + d[0]*speed, cur_pos[1] + d[1]*speed)
        self.set_pos(*new_pos)

    def get_info(self):
        info = [self.pos[0], self.pos[1], self.range, self.max_speed]
        return info 

    def get_integer_pos(self):
        cur_pos = self.get_pos()
        return (int(cur_pos[0]), int(cur_pos[1]))
    
    
class Map(MapBase):
    def __init__(self, width, height):
        super().__init__(width, height)
        

class DiscreteEnv(BaseEnv):
    def __init__(self, config:dict):
        self.config = config 
        self.n_predators = self.config['n_predators']
        self.n_preys = self.config['n_preys']
        self.width = self.config['width']
        self.height = self.config['height']
        self.predator_range = self.config['predator_range']
        self.predator_max_speed = self.config['predator_max_speed']
        self.prey_max_speed = self.config['prey_max_speed']

        dummy_prey = Prey(0,0,self.width, self.height,self.prey_max_speed)
        dummy_predator = Predator(0,0,self.width, self.height, self.predator_range, self.predator_max_speed)
        self.action_space = gym.spaces.Dict(
            {
                "prey":gym.spaces.Dict({
                    i:dummy_prey.action_space for i in range(self.n_preys)
                }),
                "predator":gym.spaces.Dict({
                    i:dummy_predator.action_space for i in range(self.n_predators)
                })
            }
        )
        self.observation_space = gym.spaces.Dict(
            {
                "prey":gym.spaces.Dict({
                    i:dummy_prey.observation_space for i in range(self.n_preys)
                }),
                "predator":gym.spaces.Dict({
                    i:dummy_predator.observation_space for i in range(self.n_predators)
                })
            }
        )
        self.map = Map(self.width, self.height)
        self.renderer = TerminalRenderer(self.width+1, self.height+1)
    


    def reset(self):
        poses = self.generate_random_positions(self.n_predators + self.n_preys, self.width, self.height)
        self.predators = [Predator(poses[i][0], 
                                    poses[i][1], 
                                    self.width, 
                                    self.height,
                                    self.predator_range,
                                    self.predator_max_speed)  for i in range(self.n_predators)
                        ] 
        self.preys = [Prey(poses[i][0]+self.n_predators, 
                            poses[i][1]+self.n_predators, 
                            self.width, 
                            self.height,
                            self.prey_max_speed)  for i in range(self.n_preys)
                        ]
        return self.get_obs()



if __name__ == "__main__":
        import time 
        from gym_predator_prey import env_creator
        import json 
        with open("../configs/Discrete.json") as f :
            config = json.load(f)
        env = env_creator(config)

        done = False 
        obs = env.reset()
        while not done:
            action = env.action_space.sample()
            next_state, reward, done, info = env.step(action)
            # print(next_state)
            done = done['__all__']
            env.render()
            time.sleep(1)
        
