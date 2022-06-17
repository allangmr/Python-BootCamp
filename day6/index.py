def jump():
    move()
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()

while not at_goal():    
    if wall_in_front():
        turn_left()
    else:        
        jump()