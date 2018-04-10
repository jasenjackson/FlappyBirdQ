def obs_to_state(env, obs):
    ### Maps the observations to a state
    ## vertical_distance =  pipe_bottom - pos_y
    ## print(vertical distance)
    ## print(horizontal distance)
    ## put vertical distance into 8 bins
    player_y = 380-obs[0]
    bottom_pipe = 512-obs[4]
    vertical_distance = bottom_pipe - player_y
    horizontal_distance = obs[2]

    #vertical_cat = int(vertical_distance/10)
    #horizontal_cat = int(horizontal_distance/10)



    #define a height category based on vertical distance to the pipe (+/-)
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
