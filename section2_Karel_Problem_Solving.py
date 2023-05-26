'''In this task, Karel will always start by standing in front of a pile of beepers. Karel needs to pick up the entire pile of beepers and spread them out along the row so that there is exactly one beeper in each cell, and exactly as many cells with beepers as were in the original pile. Karel should spread the first beeper into the cell where the pile was.'''

from karel.stanfordkarel import *

# ------------------ my codes--------------------------

def main():
    """
    Firstly, we go to the start position.
    Secondly, we take the second position in a line as start position,
    open the loop that we pick and put beepers.
    when the start position is empty, it can be broken.
    In the end, we put the last beeper into the start place. 
    """
    move() 
    while beepers_present():
        one_round()
    turn_around()
    move()
    turn_around()
    move()
    put_beeper()
    turn_around()
    move()
    turn_around()

def one_round():
    '''
    This is one action that we pick and put one beeper.
    The key is if the beeper in the start position is the last bepper.
    If it is the last one, we take it and go out of the loop to move.
    so we just take it and leave the position empty.
    when next time we go to the start position, we can stop the loop.
    If it not the last one, we take one, go to next place, put it down and go back. 
    '''
    pick_beeper()
    if no_beepers_present():
        back()
    else:
        while beepers_present():
            move()
        put_beeper()
        back()

def back():
    '''
    When we end up putting the beeper, we go back to the start position.
    Start position is the second position in one line.
    Make the precondition and the postcondition keep the same.
    Take the second position in a line as start position 
    and back to this position.
    '''
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    move()

def turn_around():
    turn_left()
    turn_left()

# ------------------ leader's codes--------------------------

# Section 2 Solutions
# from karel.stanfordkarel import *

# """
# Each row starts in front of a stack of beepers. Karel should pick them
# up, one at a time, and spread them down the row. 
# Caution! Karel can't count, and starts with infinite beepers infinite
# her bag. How can you solve this puzzle?
# """

# def main():
#     move()
#     spread()
#     step_back()
    
# def spread():
#     while beepers_present():
#         pick_beeper()
#         if beepers_present():
#             move_to_end()
#             put_beeper()
#             reset()
#     put_beeper()

# def move_to_end():
#     while beepers_present():
#         move()

# def reset():
#     turn_around()
#     move_to_wall()
#     turn_around()
#     move()

# def move_to_wall():
#     while front_is_clear():
#         move()

# def turn_around():
#     turn_left()
#     turn_left()
    
# def step_back():
#     turn_around()
#     move()
#     turn_around()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
