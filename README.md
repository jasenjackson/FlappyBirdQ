# FlappyBirdQ
Q-learning with Flappy Bird using temporal descriptive learning

<a href="http://pygame-learning-environment.readthedocs.io/en/latest/_images/flappybird.gif" title="Go Flappy, Go!">
 

## flappy.py 

Initializes a new Q_agent (class is in this file) and trains it on a designated number of episodes. It uses <b> q_agent.py </b> (should be something like obs_to_state.py) to convert observations from the getGameState() function to states for the Q table. 

## ple_env.py 

Ple_env.py for gym_ple should be updated for flappybird so replace the ple_env in your gym_ple/gym-ple/ folder with this one. It includes a function to process the game state and modified step & reset functions.
