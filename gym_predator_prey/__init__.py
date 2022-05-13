

from gym_predator_prey.envs.ContinuousEnv import ContinuousEnv
from gym_predator_prey.envs.DiscreteEnv import DiscreteEnv
from gym_predator_prey.envs.GridEnv import GridEnv

def env_creator(config):
    if config.get("env") == "grid":
        env = GridEnv(config)
    elif config.get("env") == "continuous":
        env = ContinuousEnv(config)
    elif config.get("env") == "discrete":
        env = DiscreteEnv(config)
    else:
        raise ValueError("{0} is not implemneted environment".format(config.get("env")))
    return env 