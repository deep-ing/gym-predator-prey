# gym-predator-prey

* Action space  is fixed 
* Observation space is given by full observation, hence you can use `gym.Wrapper`
* Full observation : `predator` + `prey` + `map`

## 1. Discrete 

* Predator 
  * `action_space` : {no-op, left, bottom, up, right}
  * `observation_space` : full information
  * `reward`  : `epsilon` for each time step 
* Prey
  * `action_space` : {no-op, left, bottom, up, right}
  * `observation_space` : full information
  * `reward`  : `-epsilon` for each time step 
* Map 
  * [-1,1] x [-1,1] with center (0,0)


## 2. Continuous

* Predator 
  * `action_space` : speed [0~`pd_max_speed`], angle [0~2pi]
  * `observation_space` : full information
  * `reward`  : `epsilon` for each time step 
* Prey
  * `action_space` : speed [0~`pr_max_speed`], angle [0~2pi]
  * `observation_space` : full information
  * `reward`  : `-epsilon` for each time step 
* Map 
  * [-1,1] x [-1,1] with center (0,0)


## 3. Grid 
* Predator 
  * `action_space` : {no-op, left, bottom, up, right}
  * `observation_space` : full information
  * `reward`  : `epsilon` for each time step 
* Prey
  * `action_space` : {no-op, left, bottom, up, right}
  * `observation_space` : full information
  * `reward`  : `-epsilon` for each time step 
* Map 
  * [-1,1] x [-1,1] with center (0,0)


## Code 

```python

import gym_predator_prey

env_creator = gym_predator_prey.env_creator
config = {
    "env": "grid"  # "discrete", "continuous",
    ...
}

env = env_creator(config)
...

```