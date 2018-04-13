'''
Tabular Q Learning with Flappy bird (Comp 271 Final Project)
Authors: Angie Georgaras '20, Jasen Jackson '19, Collins Mbachu '18, John Morris '19
Script: Q-learning Agent Training for Flappy bird (flappy.py)
Desription: Trains Q table on FlappyBird using OpenAi/Gym and the PyGame Learning Environment (PLE)
Q-Agent(): creates Q-Agent object that selects action based on Q-table values and the epsilon hyper-parameter
Train(): Runs the training sequence for training the Q-Agent (runs flappy bird and modifies the Q_table)

External scripts:
    - gym: provides an environment (list of usable functions) for training the agent (step, reset, etc.)
    - gym_ple: allows access to games from the PyGame Learning Environment (PLE)
    - obs-to-state: maps all observations in the game to the state functions
    - params: keeps track of all hyper-parameters

'''

import os, sys
import numpy as np
import obs_to_state
import params
import gym_ple
import gym
from gym.wrappers import Monitor

## file output
outdir = '/Users/jasenmatthewjackson/github/Comp271/Q-learning/results7'
extension = "Q-learning-"

##Q-table initialization parameters
n_vertical = 57
n_horizontal = 29

## Algorithm Hyper-params
episode_count = 4000000000
eps = 0 #epsilon = exploration factor
gamma = 1
alpha = 0.618
initial_lr = 0.618 #initial alpha
min_lr = 0.618 #minimum alpha

class Q_Agent(object):
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, a, b):
        ## take random action if random float is less than epsilon
        ## otherwise select action with highest Q-score for the given state
        if np.random.uniform(0, 1) < eps:
            return np.random.choice(env.action_space.n)
        else:
            return np.argmax(Q[a][b])

if __name__ == '__main__':

    ## setup learning environment with video recording
    env = gym.make('FlappyBird-v0' if len(sys.argv)<2 else sys.argv[1])
    env = Monitor(env, directory=outdir, force=True)
    env.seed(0)

    ## initialize the Q-agent
    agent = Q_Agent(env.action_space)
    reward, done = 0, False

    print("~~~~~~~Let's Q Learn!~~~~~~~")
    Q = np.zeros((n_vertical,n_horizontal,2)) # (number of height bins, number of distance bins, number of actions)
    for i in range(episode_count):
        #print("Episode: " + str(i))
        ob = env.reset()
        total_reward = 0
        ## decrease the learning rate as time progresses -- should you do this for flappy bird??
        while True:
            #turn a and b into states
            a, b = obs_to_state.uniform_10(env, list(ob[0]))
            #print("vertical distance: " + str(a))

            #determine action from Q-learning agent
            action = agent.act(a,b)

            #take a step in the environment
            ob, reward, done, _ = env.step(action)
            total_reward += reward

            #update q table
            a_, b_ = obs_to_state.uniform_10(env, list(ob[0]))
            Q[a][b][action] = Q[a][b][action] + alpha * (reward + gamma * np.max(Q[a_][b_]) - Q[a][b][action])
            if done:
                break


        ## print every 250 episodes
        if i % 250 == 0:
            print("Episode: " + str(i) + ", Reward: " + str(total_reward))
            # Note there's no env.render() here. But the environment still can open window and
            # render if asked by env.monitor: it calls env.render('rgb_array') to record video.
            # Video is not recorded every episode, see capped_cubic_video_schedule for details.

    # Dump the Q_table
    np.save("/Users/jasenmatthewjackson/github/Comp271/Q-learning/q_table", Q_table)

    #how to load the q_table
    #Q_table_2 = np.load("q_table.npy")
    #Q_table_2 == Q_table
    env.close()
