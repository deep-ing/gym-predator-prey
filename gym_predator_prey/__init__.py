

from gym_predator_prey.envs.PredatorPreyContinuousEnv import PredatorPreyContinuousEnv
from gym_predator_prey.envs.PredatorPreyDiscreteEnv import PredatorPreyDiscreteEnv
from gym_predator_prey.envs.PredatorPreyGridEnv import PredatorPreyGridEnv

def env_creator(config):
    if config.get("env") == "grid":
        env = PredatorPreyGridEnv(config)
    elif config.get("env") == "continuous":
        env = PredatorPreyContinuousEnv(config)
    elif config.get("env") == "discrete":
        env = PredatorPreyDiscreteEnv(config)
    else:
        raise ValueError("{0} is not implemneted environment".format(config.get("env")))
    return env 