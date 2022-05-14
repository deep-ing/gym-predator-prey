# gym-predator-prey

This environment is for meta-learning or transfer-learning experiments. Three types of envrionments are given *Discrete*, *Continuous*, and *Grid*. All the spaces have same observation space, but the action spaces are different.



* Observation space is given by full observation, hence you can use `gym.Wrapper`
* Full observation : `predator` + `prey` + `map`

## 1. Discrete 

**Discrete direction + Continuous speed**

* Predator 
  * `action_space` : {no-op, left, bottom, up, right} x [0~`max_speed`]
  * `observation_space` : full information
  * `reward`  : `-1` for each time step  / `100` when prey is caught
* Prey
  * `action_space` : {no-op, left, bottom, up, right} x [0~`max_speed`]
  * `observation_space` : full information
  * `reward`  : `1` for each time step 
* Map 
  * [0,`width`] x [0, `height`]


## 2. Continuous

**Continuous direction + Continuous speed**


* Predator 
  * `action_space` :  angle [0~2pi], speed [0~`pd_max_speed`]
  * `observation_space` : full information
  * `reward`  : `1` for each time step 
* Prey
  * `action_space` :  angle [0~2pi], speed [0~`pr_max_speed`]
  * `observation_space` : full information
  * `reward`  : `-1` for each time step 
* Map 
  * [0,`width`] x [0, `height`]


## 3. Grid 

**Discrete direction + Dontinuous speed**

* Predator 
  * `action_space` : {no-op, left, bottom, up, right}
  * `observation_space` : full information
  * `reward`  : `epsilon` for each time step 
* Prey
  * `action_space` : {no-op, left, bottom, up, right}
  * `observation_space` : full information
  * `reward`  : `-epsilon` for each time step 
* Map 
  * [0,1,2, ... `width`-1] x [0,1,2,..., `height`-1]


## Code 

```python

import gym_predator_prey

env_creator = gym_predator_prey.env_creator
config = {
    "env": "grid"  # "discrete", "continuous",
    ...
    # check gym_predator_prey/configs/Grid.json    
}

env = env_creator(config)
state = env.reset()
...

```