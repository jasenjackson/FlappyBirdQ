# FlappyBirdQ
The goal of this project is to develop a model-free Q-learning agent (in Python) that can play Flappy Bird and win indefinitely. Q-learning is a machine-learning technique that uses a "Q" function that converts non-visual state representations into meaningful actions. Here, our non-visual states or "observations" are the horizontal and vertical distance relative to the bottom pipe, and we have two actions: jump or sink. For each time step, our agent assesses its location relative to the next pipe, uses the Q-function to predict the action that will lead to the highest reward and updates the Q-function based on the reward value given from the environment. 

<center><a href="https://imgflip.com/gif/2859uo"><img src="https://i.imgflip.com/2859uo.gif" title="made at imgflip.com"/></a></a></center>

 

## flappy.py 
Initializes the agent and a Q-function (approximated using a numpy array) and trains it to run on a designated number of episodes. It uses the flappybird game from the PyGame Learning environment and openAI-gym for the reinforcement tasks. Therefore, PLE, gym-ple and gym are dependencies. The agent uses the obs_to_state function to convert continuous environmental variables to quantized state values which are subsequently fed into the Q-learning formula/algorithm. It uses <b> q_agent.py </b> (should be something like obs_to_state.py) to convert observations from the getGameState() function to states for the Q table. 

## obs_to_state.py
Converts continuous variables from the game environment (bottom pipe y position, and the player's velocity, y position and distance to the next pipe) to quantized states. The exponential() function creates bins that grow exponentially with distance from the pipe. The uniform_10() function creates uniform bins for each state that are quantized to bin every 10 values by dividing by some integer and int() converting the end value. 

## ple_env.py 
Ple_env.py in the gym_ple package should be updated for flappybird (gym_ple/gym-ple/ple_env.py). The environment contains code which processes the game state values and also modifies the reward system via the step() and reset() functions.

## params.py
Keeps track of the various parameters needed to make the program run. Cleans up the main flappy.py code. 
