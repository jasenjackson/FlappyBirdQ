'''
beginning of ple_env.py file, modified from native gym package ple_env.py to better suit our project
'''
import os
import gym
from gym import spaces
from ple import PLE
import numpy as np
#changed to match jasens
class PLEEnv(gym.Env):
    metadata = {'render.modes': ['human', 'rgb_array']}


    def __init__(self, game_name='FlappyBird', display_screen=True):
        # set headless mode
        os.environ['SDL_VIDEODRIVER'] = 'dummy'

        # open up a game state to communicate with emulator
        import importlib
        game_module_name = ('ple.games.%s' % game_name).lower()
        game_module = importlib.import_module(game_module_name)
        game = getattr(game_module, game_name)()

        #* converts non-visual state representation to numpy array
        def process_state(state):
                return np.array([ state.values() ])

        self.game_state = PLE(game, fps=30, display_screen=display_screen, state_preprocessor=process_state) #* added state_preprocessor
        self.game_state.init()
        self._action_set = self.game_state.getActionSet()
        self.action_space = spaces.Discrete(len(self._action_set))
        self.screen_height, self.screen_width = self.game_state.getScreenDims()
        #self.observation_space = spaces.Box(low=0, high=255, shape=(self.screen_width, self.screen_height, 3), dtype=np.uint8)
        #self.observation_space = spaces.Box(self.low, self.high)
        self.viewer = None



    def _step(self, a):
        reward = self.game_state.act(self._action_set[a])
        state = self.game_state.getGameState()
        terminal = self.game_state.game_over()

        '''
        reward system:
        did you die? -1000
        else +1
        '''
        if terminal == True:
            reward = -1000
        else:
            reward = 1


        return state, reward, terminal, {}

    def _get_image(self):
        image_rotated = np.fliplr(np.rot90(self.game_state.getScreenRGB(),3)) # Hack to fix the rotated image returned by ple
        return image_rotated

    @property
    def _n_actions(self):
        return len(self._action_set)

    # return: (states, observations)
    def _reset(self):
        #self.observation_space = spaces.Box(low=0, high=255, shape=(self.screen_width, self.screen_height, 3), dtype=np.uint8)
        self.game_state.reset_game()
        state = self.game_state.getGameState()
        return state

    def _render(self, mode='human', close=False):
        if close:
            if self.viewer is not None:
                self.viewer.close()
                self.viewer = None
            return
        img = self._get_image()
        if mode == 'rgb_array':
            return img
        elif mode == 'human':
            from gym.envs.classic_control import rendering
            if self.viewer is None:
                self.viewer = rendering.SimpleImageViewer()
            self.viewer.imshow(img)


    def _seed(self, seed):
        rng = np.random.RandomState(seed)
        self.game_state.rng = rng
        self.game_state.game.rng = self.game_state.rng

        self.game_state.init()
#end of ple_env.py file
