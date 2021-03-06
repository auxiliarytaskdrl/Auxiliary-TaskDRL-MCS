import sys
import os

from Reinforce_Method.Random import *
from Reinforce_Method.Greedy import *
from Config.config import *
from Reinforce_Method.MC_PG import *
from Reinforce_Method.Actor_Critic import *
from Reinforce_Method.PPO import *
from Data_Generator.env_trajectory import *

if __name__ == "__main__":
    os.environ["CUDA_VISIBLE_DEVICES"] = '1'

    # Environment
    if sys.argv[1] == "RANDOM":
        config = Random_config()
        game = "random_trj"
        env = env_trajectory(game, config)
        rand = Random(config, game, env)
        rand.run_test(10)
    elif sys.argv[1] == "GREEDY":
        config = Greedy_config()
        game = "greedy_trj"
        env = env_trajectory(game, config)
        greedy = Greedy(config, game, env)
        greedy.run_test(config, 30)
    elif sys.argv[1] == "AC":
        config = Traffic_config()
        game = "trajectory"
        env = env_trajectory(game, config)
        AC = Actor_Critic(config, game, env)
        AC.Policy_Iteration()
    elif sys.argv[1] == "MC_PG":
        config = Traffic_config()
        game = "trajectory"
        env = env_trajectory(game, config)
        PG = MC_PG(config, game, env)
        PG.Policy_Iteration()
    elif sys.argv[1] == "PPO":
        config = Traffic_config()
        game = "trajectory"
        env = env_trajectory(game, config)
        PG = PPO(config, game, env)
        PG.Policy_Iteration()
