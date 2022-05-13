
import gym 
import numpy as np 
class BaseEnv(gym.Env):
    def __init__(self):
        self.predators = None 
        self.preys = None 

    def take_predator_actions(self, predator_actions):
        for k, action in predator_actions.items():
             
            self.predators[k].take_action(action)

    def take_prey_actions(self, prey_actions):
        for k, action in prey_actions.items():
            self.preys[k].take_action(action)

    def apply_collison(self):
        for predator in self.predators:
            for prey in self.preys:
                if prey.is_alive():
                    prey_pos = prey.get_pos()
                    predator_pos = predator.get_pos()
                    if np.linalg.norm(np.array(predator_pos) - np.array(prey_pos)) < predator.range:
                        prey.reduce_hp_by_1()
                        predator.increase_eaten_by_1()

    def make_predators_hungry(self):
        for predator in self.predators:
            predator.become_hungry()
    
    def step(self, multi_action):
        """
        {"prey" : {
            0 :1 ,
            1 :2,
            }
        "predator":{
            1:3,
            2:4
            }
        }

        """
        prey_actions = multi_action['prey']
        predator_actions = multi_action['predator']
        self.take_prey_actions(dict(prey_actions))
        self.take_predator_actions(dict(predator_actions))
        self.apply_collison()

        rewards = {
            "prey":{
                i: 1 if prey.is_alive() else 0 for i, prey in enumerate(self.preys) 
            },
            "predator":{
                i: 10 if predator.is_satisfied else -1 for i, predator in enumerate(self.predators)
            }
        }

        dones = {
                "predator":{
                    i:False for i, predator in enumerate(self.predators)
                }, 
                "prey":{
                    i: False if prey.is_alive() else True for i, prey in enumerate(self.preys) 
                }
        }

        dones['__all__'] = all(dones['prey'].values())
        infos = {}
        self.make_predators_hungry()
        return self.get_obs(), rewards, dones, infos

    def render(self):
        predator_positions = [predator.get_integer_pos() for predator in self.predators] 
        prey_positions = [prey.get_integer_pos() for prey in self.preys if prey.is_alive()] 
 
        self.renderer.render(predator_positions, prey_positions)

    def generate_random_positions(self, n, width, height):
        positions = [] 
        distance = np.sqrt(width * height) / n
        while len(positions) < n:
            x_candidate = np.random.random() * self.width 
            y_candidate = np.random.random() * self.height 
            possible =True 
            for pos in positions:
                if np.linalg.norm(np.array(pos) - np.array([x_candidate, y_candidate])) < distance:
                    possible = False 
            if possible:
                positions.append([x_candidate, y_candidate])
        return positions 

    def get_obs(self):
        obs = {
            "prey":{
                i:prey.get_info() for i, prey in enumerate(self.preys)
            },
            "predators":{
                i:predator.get_info() for i, predator in enumerate(self.predators)
            }
        }
        return obs

