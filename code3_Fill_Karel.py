from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    for i in range(5):
        round()

    
def round():
    while front_is_clear():
        check_put()
    turn_around()
    while front_is_clear():
        check_put()
    condition_test()
            
def condition_test():
    if right_is_clear():
        turn_right()
        move()
        turn_right()
    else:
        turn_around()
        while front_is_clear():
            move()

def check_put():
    if no_beepers_present():
        put_beeper()
    move()
    
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
