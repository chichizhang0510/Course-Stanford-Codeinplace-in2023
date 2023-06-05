''' 1.asks the user for their height in meters and prints whether or not they are the correct height to be a NASA astronaut.'''
def main():
    # TODO write your solution here
    # ask the user the height
    height = float(input("What is your height? "))
    # check the condition
    condition(height)
    
    
def condition(height):
    if height>1.6 and height<1.9:
        print("Correct height to be an astronaut")
    elif height <= 1.6:
        print("Below minimum astronaut height")
    elif height >=1.9:
        print("Above maximum astronaut height")

if __name__ == "__main__":
    main()
    
    
''' 2.Print out each of the numbers 1 through 100 and whether that number is even or odd.
100 is specified using a constant MAX_NUMBER.
Here is what the output looks like when MAX_NUMBER = 100
'''

# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100

def main():
    pass
    # TODO: your code here
    for number in range(1, MAX_NUMBER+1):
        check(number)
        number +=1
        
def check(number):
    if number%2==1:
        print(f"{number} is odd")
    else:
        print(f"{number} is even")

if __name__ == "__main__":
    main()
    
    
'''3.Write a program that has Karel draw four small "waves". Each wave is a triangle made up of three beepers. There is a gap between each wave.'''

from karel.stanfordkarel import *

def main():
    # TODO: your code here
    while front_is_clear():
        triangle()



def triangle():
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    turn_around()
    move()
    turn_left()
    if front_is_clear():
        move()
        move()


def turn_around():
    turn_left()
    turn_left()

# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
    
    
'''4.A simple way to achieve great things in life is to make small forward progress every day. Non-decreasing progress is one of the principles behind modern AI.

Write a program that asks the user to enter a sequence of "non-decreasing" numbers one at a time. Numbers are non-decreasing if each number is greater than or equal to the last.

When the user enters a number which is smaller than their previously entered value, the program is over. Tell the user how long their sequence was.'''


def main():
    # TODO write your solution here
    print("Enter a sequence of non-decreasing numbers.") 
    
    loop = True
    i=0
    first_number = float(input("Enter num: "))
    while loop:
        second_number = float(input("Enter num: "))
        i+=1
        if first_number <= second_number:
            first_number = second_number
        else:
            loop = False
            print(f"Thanks for playing!\nSequence length: {i}")


if __name__ == "__main__":
    main()
    
    
# Consider the following buggy code:

from graphics import Canvas

def main():
    # draws two cars
    canvas = Canvas(400, 400)
    x = 10
    y = 10
    draw_car()

    x = 100
    y = 100
    draw_car()

def draw_car():
    # draws a car at the location x, y
    # you can assume that math offsets for the rectangles are correct
    canvas.create_rectangle(x, y, x + 50, y + 20)
    canvas.create_rectangle(x + 10, y - 10, x + 40, y + 20)

if __name__ == '__main__':
    main()
  
'''5.Fix this program so that it does what it is meant to. You can make changes to both draw_car and main, but draw_car must implement the functionality described in its comment. Write a comments for each line you changed.

Note that you should assume that the offsets in draw_car are correct. You are not meant to be worrying about the canvas coordinates, rather the control flow of the program.'''
    
# CORRECT CODES
from graphics import Canvas

def main():
    # draws two cars
    canvas = Canvas(400, 400)
    x = 10
    y = 10
    draw_car(canvas, x, y) # put the valid variables into the function

    x = 100
    y = 100
    draw_car(canvas, x, y) # put the valid variables into the function

def draw_car(canvas, x, y): # put the valid variables into the function
    # draws a car at the location x, y
    # you can assume that math offsets for the rectangles are correct
    canvas.create_rectangle(x, y, x + 50, y + 20)
    canvas.create_rectangle(x + 10, y - 10, x + 40, y + 20)

if __name__ == '__main__':
    main()
