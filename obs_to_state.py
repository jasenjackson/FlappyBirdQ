'''
beginning of obs_to_state.py file
Tabular Q Learning with Flappy bird (Comp 271 Final Project)
Authors: Angie Georgaras '20, Jasen Jackson '19, Collins Mbachu '18, John Morris '19
Script: Observation to State (obs-to-state.py)
Desription: Maps all observations to the state space for the Q table.
exponential(): creates bins that grow exponentially with vertical_distance from the pipe.
uniform_10(): creates uniform bins for each state by dividing by 10 and converting to int()

'''

def uniform_10(env, obs):
    ## player y and bottom_pipe are defined from the bottom
    ## vertical_distance is the difference between the two, wherenegative
    ## negative is below the pipe and positive is above.
    ## potentially set a_max and b_max as parameters?

    screen_height = 512
    player_y = ((screen_height-obs[0])) #381 is the max value, 0 is the min ()
    bottom_pipe = (screen_height-obs[4]) #512 is the max value, 220 is the min ()
    vertical_distance = int(player_y - bottom_pipe) ## this can range from -256 to 292 (?)
    horizontal_distance = int(obs[2]/10) ## 29 possible states? Rough calculation

    ## TODO:
    ## to make the above method work, we need to know the number of values (observation space)
    ## that this can generate in order to define the q_table[a][b]. Is there a mathematical expression
    ## we could use for this?

    state_hd = 0
    state_vd = 0
    if vertical_distance <= -1 and vertical_distance >= -9:
        state_vd = -30
    else:
        state_vd = int(vertical_distance/10)
    state_hd = int(horizontal_distance/10)

    #print("state_vd: " + str(vertical_distance) + ", state: " +  str(state_vd))

    return state_vd, state_hd



def exponential(env, obs):
    ## player y and bottom_pipe are defined from the bottom
    ## vertical_distance is the difference between the two, wherenegative
    ## negative is below the pipe and positive is above.
    player_y = 512-obs[0]
    bottom_pipe = 512-obs[4]
    vertical_distance = bottom_pipe - player_y
    horizontal_distance = obs[2]

    height_cat = 0
    if vertical_distance < 0:
        height_cat = 0
    if vertical_distance < 2:
        height_cat = 1
    elif vertical_distance < 4:
        height_cat = 2
    elif vertical_distance < 8:
        height_cat = 3
    elif vertical_distance < 16:
        height_cat = 4
    elif vertical_distance < 32:
        height_cat = 5
    elif vertical_distance < 64:
        height_cat = 6
    elif vertical_distance < 128:
        height_cat = 7
    elif vertical_distance < 256:
        height_cat = 8
    else: # very far (above)
        height_cat = 9

    #define a distance category based on vertical distance to the pipe (+/-)
    dist_cat = 0
    if horizontal_distance < 8: ## mid
        dist_cat = 0
    elif horizontal_distance < 16: ## far
        dist_cat = 1
    elif horizontal_distance < 32: ## mid
        dist_cat = 2
    elif horizontal_distance < 64: ## mid
        dist_cat = 3
    elif horizontal_distance < 100: ## mid
        dist_cat = 4
    elif horizontal_distance < 125: ## mid
        dist_cat = 5
    elif horizontal_distance < 150:
        dist_cat = 6
    elif horizontal_distance < 175:
        dist_cat = 7
    elif horizontal_distance < 200:
        dist_cat = 8
    else: # very far
        dist_cat = 9

    #print("(vd,vc,hd,hc): (" + str(vertical_distance) + "," + str(vertical_cat) + "," + str(horizontal_distance) + "," + str(horizontal_cat) + ")")
    return height_cat, dist_cat
#end of obs_to_state.py file
