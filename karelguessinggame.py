"""
----------------------------------------------------------------
                      Karel's Guessing Game
 Welcome to Karel's Guessing Game! In this simulation, you will
 have 3 chances to determine which location the ball that Karel
  wants is at. Choose between 3 levels to try and find where
                    Karel's special ball is at!
----------------------------------------------------------------
"""

"""
----------------------------------------------------------------
                    User Input - Enter Values
  Enter values for any of the 3 levels here. To change level,
   go to the dropdown menu for "World" on the output portion
 of the program. Then, chose between Levels 1 and 3. It is best
    to reset the program once you have completed a level.

 IMPORTANT: ENTER THE LEVEL NUMBER BELOW FOR THE PROGRAM TO WORK
----------------------------------------------------------------
"""
# ENTER LEVEL NUMBER HERE (MIN 1, MAX 3)
level_num = 1 # Placeholder Value, Change If Needed

# Guess 1 - X/Avenue Coordinate (MIN 1, MAX 10)
x1 = 1 # Placeholder Value, Change If Needed
# Guess 1 - Y/Street Coordinate (MIN 1, MAX 10)
y1 = 1 # Placeholder Value, Change If Needed

# Guess 2 - X/Avenue Coordinate (MIN 1, MAX 10)
x2 = 6 # Placeholder Value, Change If Needed
# Guess 2 - Y/Street Coordinate (MIN 1, MAX 10)
y2 = 3 # Placeholder Value, Change If Needed

# Guess 3 - X/Avenue Coordinate (MIN 1, MAX 10)
x3 = 6 # Placeholder Value, Change If Needed
# Guess 3 - Y/Street Coordinate (MIN 1, MAX 10)
y3 = 6 # Placeholder Value, Change If Needed

"""
----------------------------------------------------------------
        DO NOT MESS WITH BELOW - PROGRAM ESSENTIALS
----------------------------------------------------------------
"""
# Variables - Used To Store Random x & y Values + Karel Position
x = 0
y = 0
lx = 1
ly = 1

"""
Precondition: Level number & (x,y)/(Av, St) values remain how
              they were inputted by user
Postcondition: Level number & (x,y)/(Av, St) values set to
               default value of 1
"""
# Function Checks All Input Numbers If They Meet Restriction (Cancels Or Updates User Input As Failsafe)
def check_points():
    global x1, y1, x2, y2, x3, y3, level_num
    if level_num < 1:
        pass
    elif level_num > 3:
        pass
    if x1 < 1:
        x1 = 1
    elif x1 > 10:
        x1 = 1
    if y1 < 1:
        y1 = 1
    elif y1 > 10:
        y1 = 1
    if x2 < 1:
        x2 = 1
    elif x2 > 10:
        x2 = 1
    if y2 < 1:
        y2 = 1
    elif y2 > 10:
        y2 = 1
    if x3 < 1:
        x3 = 1
    elif x3 > 10:
        x3 = 1
    if y3 < 1:
        y3 = 1
    elif y3 > 10:
        y3 = 1
        
check_points()

# Checks Level Number To Determine Random Ball Selection
if level_num == 1:
    x = 6
    y = 6
elif level_num == 2:
    for j in range(1, 7):
        if random_chance(0.166):
            x = j
            break
    for k in range(5, 11):
        if random_chance(0.166):
            y = k
            break
    if x == 0:
        x = 6
    if y == 0:
        y = 6
elif level_num == 3:
    for l in range(1, 11):
        if random_chance(0.166):
            x = l
            break
    for m in range(1, 11):
        if random_chance(0.166):
            y = m
            break
    if x == 0:
        x = 1
    if y == 0:
        y = 1

"""
Precondition: User has inputted values. Karel is facing east.
Postcondition: All values have been checked. If at least one of the
               values are correct, Karel will highlight the square
               green and take ball and the program will end. If one 
               or more of the values are incorrect, then Karel will
               highlight that square in orange and collect the ball.
               If all 3 guesses are marked orange, then the program
               will end.
"""
# Checks Guesses (Right/Wrong)
def check_guess():
    global x1, y1, x2, y2, x3, y3, lx, ly
    if x1 != x or y1 != y:
        for i in range(x1-1):
            move()
        turn_left()
        for i in range(y1-1):
            move()
        turn_right()
        if balls_present():
            take_ball()
        paint(color["orange"])
        lx = x1
        ly = y1
        
    if x1 == x and y1 == y:
        for i in range(x1-1):
            move()
        turn_left()
        for i in range(y1-1):
            move()
        turn_right()
        if balls_present():
            take_ball()
        paint(color["green"])
        lx = x1
        ly = y1
        x2 = x1
        y2 = y1
        x3 = x1
        y3 = y1
        
    if x2 != x or y2 != y:
        if x2 == lx:
            pass
        elif x2 < lx:
            turn_around()
            for i in range(lx-x2):
                move()
            turn_around()
        elif x2 > lx:
            for i in range(x2-lx):
                move()
        if y2 == ly:
            pass
        elif y2 < ly:
            turn_right()
            for i in range(ly-y2):
                move()
            turn_left()
        elif y2 > ly:
            turn_left()
            for i in range(y2-ly):
                move()
            turn_right()
        if balls_present():
            take_ball()
        paint(color["orange"])
        lx = x2
        ly = y2
        
    if x2 == x and y2 == y:
        if x2 == lx:
            pass
        elif x2 < lx:
            turn_around()
            for i in range(lx-x2):
                move()
            turn_around()
        elif x2 > lx:
            for i in range(x2-lx):
                move()
        if y2 == ly:
            pass
        elif y2 < ly:
            turn_right()
            for i in range(ly-y2):
                move()
                turn_left()
        elif y2 > ly:
            turn_left()
            for i in range(y2-ly):
                move()
            turn_right()
        if balls_present():
            take_ball()
        paint(color["green"])
        lx = x2
        ly = y2
        x3 = x2
        y3 = y2
        
    if x3 != x or y3 != y:
        if x3 == lx:
            pass
        elif x3 < lx:
            turn_around()
            for i in range(lx-x3):
                move()
            turn_around()
        elif x3 > lx:
            for i in range(x3-lx):
                move()
        if y3 == ly:
            pass
        elif y3 < ly:
            turn_right()
            for i in range(ly-y3):
                move()
            turn_left()
        elif y3 > ly:
            turn_left()
            for i in range(y3-ly):
                move()
            turn_right()
        if balls_present():
            take_ball()
        paint(color["orange"])
        
    if x3 == x and y3 == y:
        if x3 == lx:
            pass
        elif x3 < lx:
            turn_around()
            for i in range(lx-x3):
                move()
            turn_around()
        elif x3 > lx:
            for i in range(x3-lx):
                move()
        if y3 == ly:
            pass
        elif y3 < ly:
            turn_right()
            for i in range(ly-y3):
                move()
            turn_left()
        elif y3 > ly:
            turn_left()
            for i in range(y3-ly):
                move()
            turn_right()
        if balls_present():
            take_ball()
        paint(color["green"])
        
check_guess()
