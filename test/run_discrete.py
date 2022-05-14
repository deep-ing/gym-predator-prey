from gym_predator_prey import env_creator
import json 
import time 
with open("../gym_predator_prey/configs/Discrete.json") as f :
    config = json.load(f)
config['prey_max_speed'] = 2
config['predator_max_speed'] = 2
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
        env.render()
        time.sleep(0.5)