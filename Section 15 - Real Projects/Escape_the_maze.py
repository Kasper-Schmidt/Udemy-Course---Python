# Reeborg's world maze game

#these functions do exist on the platform, i just added them here, so i dont have the mistaken underlines
def turn_left():
    pass

def at_goal():
    pass

def right_is_clear():
    pass

def move():
    pass

def front_is_clear():
    pass


# Game starts from here
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear(): # Dette gør jeg først, fordi ellers kan man risikere at i et endless firkantet move, med kun koden under
    move()

turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    
