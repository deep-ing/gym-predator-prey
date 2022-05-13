import unittest


class Test(unittest.TestCase):
    def test_discrete(self):
        from gym_predator_prey import env_creator
        import json 
        with open("../gym_predator_prey/configs/Discrete.json") as f :
            config = json.load(f)
        env = env_creator(config)
        count = []
        for i in range(15):
            done = False 
            obs = env.reset()
            count.append(0)
            while not done:
                action = env.action_space.sample()
                next_state, reward, done, info = env.step(action)
                # print(next_state)
                done = done['__all__']    
                count[-1] +=1 
        print("Discrete Timesteps:",count)
        

    def test_continuous(self):
        from gym_predator_prey import env_creator
        import json 
        with open("../gym_predator_prey/configs/Continuous.json") as f :
            config = json.load(f)
        env = env_creator(config)
        count = []
        for i in range(15):
            done = False 
            obs = env.reset()
            count.append(0)
            while not done:
                action = env.action_space.sample()
                next_state, reward, done, info = env.step(action)
                # print(next_state)
                done = done['__all__']    
                count[-1] +=1 
        print("Continuous Timesteps:",count)
        

    def test_grid(self):
        from gym_predator_prey import env_creator
        import json 
        with open("../gym_predator_prey/configs/Grid.json") as f :
            config = json.load(f)
        env = env_creator(config)
        count = []
        for i in range(30):
            done = False 
            obs = env.reset()
            count.append(0)
            while not done:
                action = env.action_space.sample()
                next_state, reward, done, info = env.step(action)
                # print(next_state)
                done = done['__all__']    
                count[-1] +=1 
        print("Grid Timesteps:",count)