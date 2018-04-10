import logging
import os, sys
import numpy as np
import gym
import q_agent
from gym.wrappers import Monitor
import gym_ple


## parameters 4,000,000,000,000
episode_count = 4000000000000
eps = 0
gamma = 1
initial_lr = 0.618
min_lr = 0.618

class Q_Agent(object):
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, a, b, q, n):
        eps = (1 / n)
        if np.random.uniform(0, 1) < eps:
            return np.random.choice(env.action_space.n)
        else:
            return q

if __name__ == '__main__':
    # You can optionally set up the logger. Also fine to set the level
    # to logging.DEBUG or logging.WARN if you want to change the
    # amount of output.
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    env = gym.make('FlappyBird-v0' if len(sys.argv)<2 else sys.argv[1])
    outdir = '/Users/jasenmatthewjackson/github/Comp271/Q-learning/results7'
    env = Monitor(env, directory=outdir, force=True)

    # This declaration must go *after* the monitor call, since the
    # monitor's seeding creates a new action_space instance with the
    # appropriate pseudorandom number generator.
    env.seed(0)
    agent = Q_Agent(env.action_space)
    reward = 0
    done = False

    print("Let's Q Learn!")
    Q_table = np.zeros((10,10,2)) # (number of height bins, number of distance bins, number of actions)
    N_table = np.zeros((10,10,2))
    lr = initial_lr
    for i in range(episode_count):
        ob = env.reset()
        print(ob)
        total_reward = 0
        ## decrease the learning rate as time progresses -- should you do this for flappy bird??
        while True:
            #turn a and b into states
            a, b = q_agent.obs_to_state(env, list(ob[0]))

            ##update alpha
            approx = np.argmax(Q_table[a][b]) #get approximaiton of q
            N_table[a][b][approx] += 1 #= N[a][b][q_approx] + 1 #increment N(s,a)
            N = N_table[a][b][approx] # set N to N(s,a)
            lr = 1 / N #update alpha based on N(s,a)

            ##determine action from Q-learning agent
            action = agent.act(a,b,approx,N)

            ob, reward, done, _ = env.step(action)
            # add (a,b,t) to feedback table
            # t += 1
            total_reward += reward

            # update q table
            a_, b_ = q_agent.obs_to_state(env, list(ob[0]))
            Q_table[a][b][action] = Q_table[a][b][action] + lr * (reward + gamma * np.max(Q_table[a_][b_]) - Q_table[a][b][action])
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
