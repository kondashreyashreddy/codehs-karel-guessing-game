"""
------------------------------------------------------------
                    Karel's Drawing Tool
////////////////////////////////////////////////////////////
    Welcome to Karel's Drawing Tool, a basic drawing
      tool coded from the CodeHS SuperKarel coding 
    lab. Use the Sandbox Drawing variables to create
                    your simple drawing.
------------------------------------------------------------
"""
"""
------------------------------------------------------------
                      Sandbox Drawing
------------------------------------------------------------
"""
# Edit this variable to move Karel a certain amount of steps.    ##
# Maximum: 14                                                    ##
x = write number here
# Edit this variable to create a ball tower at a certain height. ##
# Maximum: 15                                                    ##
y = write number here
# Edit this variable to create a square with a certain length.   ##
# Dependant on x value                                           ##
# Maximum: 15                                                    ##
z = write number here
"""
------------------------------------------------------------
                  DO NOT MESS WITH BELOW
------------------------------------------------------------
"""
# Precondition: Karel facing east
# Postcondition: Karel facing east, has moved x amt times from starting
#                position
def summon_x():
    for i in range (x):
        move()

# Precondition: Karel is at x position facing east
# Postcondition: Karel is at x position facing east, he has just stacked
#                a tower that is y balls tall
def summon_y():
    turn_left()
    for i in range (y-1):
        put_ball()
        move()
    put_ball()
    turn_around()
    for i in range (y-1):
        move()
    turn_left()

# Precondition: Karel is at x position facing east
# Postcondition: Karel is at x position facing east, he has just created
#                a square that has a length of z units. 
def summon_z():
    h = 15 - x
    if z <= h:
        for i in range (4):
            for i in range (z-1):
                put_ball()
                move()
            turn_left()
    else:
        pass

if x > 0:
    summon_x()
elif x < 15:
    pass
else:
    pass

if y > 0:
    summon_y()
elif x < 16:
    pass
else:
    pass

if z > 0:
    summon_z()
else:
    pass
