# Code-in-place-in-2023
one collection of all the exercises of the Stanford Code in Place course

# 4.27 1st class

define a function

use the function

import a package

anatomy of a program

> import
>
> main function
>
> helper function
>
> start program
>
> ![1682562594776](code in place.assets/1682562594776.png)



code blocks

# 4.27 2nd class

control flow

recap

comment

descriptive naming, lower word and underscore

conditions 

loops (how many times will loop : while-no or for-yes) (postcondition matches precondition)

control flow

> ![1682568894096](code in place.assets/1682568894096.png)

beepers_present



# code1 :  Jigsaw Karel
complete this puzzle made up of beepers

# code2 :  2023 Karel
placing 20 beepers, moving Karel one step, placing 23 beepers, and moving Karel one more step

# section1 : Hospital Karel
1. Karel starts facing east at (1, 1) with an infinite number of beepers in its beeper bag.
2. The beepers indicating the positions at which hospitals should be built will be spaced so that there is room to build the hospitals without overlapping or hitting walls.
3. You will not have to build a hospital that starts in the last column.

# 5.05  3rd class

**goal :** approach to "top down" by decomposition (stepwise refinement)

**decomposition :** take the big problem into small pieces

**key :** what is the difference between success and not

**precondition** and **postcondition** must be the same

![1683287147808](code in place.assets/1683287147808.png)

> we find  the way which makes precondition and postcondition keep the same.

## **refinement**

关键思想是你应该**从顶部开始设计**你的程序，它指的是程序在概念上最高和最抽象的层次。

重要的是要查看分解的每个级别

## Iterative testing

警告：尝试编写整个程序而不进行测试是很危险的。如果你犯了错误，将很难找到错误。

作为指导原则，如果您有一个复杂的循环，请在编写整个循环之前测试循环体。

通常，通过观察最初看起来特殊的情况可以用与更一般情况完全相同的方式来处理，可以使程序变得更简单。

## Function preconditions and postconditions

当你定义一个函数时，如果你准确地写下前置条件和后置条件是什么，那么你遇到的麻烦就会少得多。

完成后，您需要确保您编写的代码始终满足后置条件，假设前提条件一开始就已满足。

> functions
>
> loops : for 
>
> if / else statement
>
> ![1683289747878](code in place.assets/1683289747878.png)
>
> infinite loop
>
> pre / post that do not match

## section meeting

finish the exercises

# 5.05 4th class

## rules of naming variable

descriptive and in snake case

> 1. start with a letter / underscore
> 2. only letter / digits / underscore
> 3. can not be a build-in command in python
> 4. case sensitive

## data types

integer : int

float : real number value

string : text characters

boolean : logical values

> why do we have int and float?

## transformation

```python
int()
str()
float()
```

## concatenate string

```python
+
```

## print spaces

```python
print("x =",x,"and y =",y)
# do not need to tranform type
```

##  Python Reader

### Interpreted vs Compiled

Python is what’s known as an **interpreted language**. When you run code in an interpreted language, another program called the **interpreter** reads your code and tells the computer what to do. This is different from other languages like Java or C++, which are **compiled languages**. With a compiled language, a **compiler** translates your code into **binary**, the language your computer understands. The computer itself then reads that binary and runs it. 

### distinction between single and block comments

*a single-line comment is fully ignored* by the interpreter, while *a block comment is valid code* that has no effect on the outcome of the program. If the interpreter sees a hashtag, it thinks to itself, “Great, I can skip this part!” With block comments, however, the interpreter doesn’t ignore the comment at all; it's just that the comment isn’t an instruction per se. The interpreter just reads it as, “Ok, there’s a comment here!” and continues on.

All of this really just means that you need to properly indent your block comments if you nest them inside of something like a loop. If you forget, Python will either yell at you for not indenting correctly, or worse, your code will break. If the block comment is not nested inside of anything, you can safely leave it unindented.

### Console

The console is where you will see error messages, prompts for user input, and output from print statements

To run a program in the  console, you write your program name after the keyword python:

python [filename.py](http://filename.py)

### print

The text you give **print** is called an **argument**

### Escape Characters

| **Code** | **Meaning**  | **Example**          | **Result**          |
| -------- | ------------ | -------------------- | ------------------- |
| \’       | Single Quote | ‘I\’m a programmer!’ | I’m a programmer    |
| \n       | New Line     | “Good\nMorning”      | GoodMorning         |
| \t       | Tab          | “Code\tIn Place”     | Code       In Place |
| \b       | Backspace    | ‘Pytho\bn’           | Pythn               |

### input

# code3 :  Fill Karel 
no matter the size of the world, Karel should fill it with beepers.

# code4 :  Hello Name 
Write a customizable version of the classic "hello world!" program in `main.py` which, instead of saying "hello world!", prompts the user for their name and then says hello to them! 

# section2 : **Karel Problem Solving**
In this task, Karel will always start by standing in front of a pile of beepers. Karel needs to pick up the entire pile of beepers and spread them out along the row so that there is exactly one beeper in each cell, and exactly as many cells with beepers as were in the original pile. Karel should spread the first beeper into the cell where the pile was.


# 5.09 5th class : expressions

## expressions

### get input

### arithmetic operators

addition+ \ subtraction- \ multiplication* \ division/ \ integer division// \ remainder% \ exponentiation \ negation

### precedence

**()** —— ****** —— - —— ***,/,//,%** —— **+,-**

> operators in same predencence categpry are evaluated left to right

### type conversion

exponentiation depends on the result

float sometimes is not exact

### shorthands

## constants

is outside (before) the function

## math library

```python
import math

# build-in constants
math.pi
path.e

# useful function
math.sqrt(x) # square root
math.exp(x) # exponent
math.log(x) 
```

## random numbers

```python
import random

# pseudorandom number : use seed
random.randint(min,max) # integer (inclusive)
random.random() # real number between 0~1
random.uniform(min,max) # real number
random.seed(x) # set seed for random number
```

## dice simulator

## reading

###   REPL : **Read**-**Eval**-**Print Loop**

```
To use REPL in the terminal, you can simply type python: 
$ python
>>> 

You can exit the REPL by pressing Ctrl+D and you should see your normal starting terminal line: 
$ python
>>> [Ctrl+D]
$ 
```

>The triple arrow shows up to let you know that you have entered the REPL. You can type any line of python code and hit enter and then the terminal will read the line, evaluate it, and print the results out to the user just like we would see in the Python Console!

###  Basic Arithmetic 

**how to account for conversion loss**?

it is important to note that the int() function simply chops off anything after the decimal. No rounding is involved. This can be dangerous. If we convert a float to an int and then back again, we might lose information. This is called **conversion loss.**

### random

###  Advanced Arithmetic 

| Operation        | Symbol  | Example                   |
| ---------------- | ------- | ------------------------- |
| Integer Division | **//**  | $ python>>> 10 // 42      |
| Exponentiation   | ***\*** | >>> 2 ** 38>>> 2 ** -10.5 |
| Modulus          | **%**   | >>> 8 % 32                |
| Unary Negation   | **-**   | >>> x = 0.5>>> -x-0.5     |

```python
def main(): 
    x = 36.0 // 10
    y = -5 // 2
    print(x) # 3.0
    print(y) # -3

if __name__ == '__main__':
    main()
```

>The second example is just meant to show what rounding down looks like for negative numbers. -5 / 2 is -2.5 and because integer division rounds down instead of truncating the value, the result is -3 (since -3 is less than -2). 

#### Precedence

**highest**

| () parentheses    |
| ----------------- |
| ** exponentiation |
| -   negation      |
| *  /  //  %       |
| +  -              |
| comparison        |
| not               |
| and or            |

**lowest**

```python
import math

def main(): 
    ans = math.exp(math.sqrt(-1) * math.pi)
    ans += 1
    print(ans)

if __name__ == '__main__':
    main()
```

>We’ve reached an error 🛑. Negative numbers are outside of the domain of square roots, so when we try to call math.sqrt(-1) we get an error. The same is true for calling math.log() on zero or negative numbers.

 # code5 :  Mad Libs 

Edit constant for to have the value 

# code6 : Multiply Two Numbers

Write a Python program that takes two integer inputs from the user and calculates the value of the first number multiplied with the second. 


# 5.10 6th class : [Control Flow](https://codeinplace.stanford.edu/cip3/learn/lesson-6-overall)

## recap

what is variable?

how to create, modify, use the variable?

binary operators

## while / if

condition is boolean that is either true or false

### create the evaluation mechanism by ourselves

comparison operators

> **==** / **!=** / **<** / **>** / **<=** / **>=**

algebraic relation

## booleans

logical operator

> **not** / **and** / **or**

can chain tests in condition as in algebra

precedence

> **arithmetic** > **comparison** > **not** > **and/or**

boolean variables

```python
x = 1 < 2 # True
y = 5.0 == 4.0 # False
c = True
```

## for loops

## reading

###  Conditionals 

Comparison Operations

Logical Operations

Logical Expressions

Precedence : use parentheses 

### Loops 

For vs While Loops

For Loops

range()

While Loops

Infinite Loops

# code7 : Joke Bot

Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: **Joke**. 

# code8 : Random Numbers

The starter code for this program prints out a single random number in the range 1 to 100, inclusive. Modify this program so that instead of printing one random number, it prints 10. 

# code9 : Double It 

Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

# code10 : Liftoff 

Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output `Liftoff!`

# **5.18**  Lesson 7 : graphics

```python
from graphics import Canvas

# create the canvas : canvas(weight,height)
# origin point (0,0)
canvas = Canvas(800,200)

# create a blue rectangle 
# high left point is in (20,20)
# low right point is in (100,100)
# the default color is black 
canvas.create_rectangle(20,20,100,100,"blue")

# create a line
canvas.create.line(0,0,800,200)

# create an "品红" oval
canvas.create_oval(250,150,500,500,"magenta")

# create an image
canvas.create_image(10,180,"image.png")

# create a text
canvas.create_text(50,20,"Programming is Awesome!!!",color="green",font="Courier",font_size=20)
```

```python
# create a centered square
from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
SQUARE_SIZE = 100

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # get the middle of the canvas
    middle_x = CANVAS_WIDTH/2
    middle_y = CANVAS_HEIGHT/2
    
    # calculate the top left corner position
    left_x = middle_x - SQUARE_SIZE/2
    top_y = middle_y - SQUARE_SIZE/2
    
    # calculate the right and bottom of the square
    right_x = left_x + SQUARE_SIZE
    bottom_y = top_y + SQUARE_SIZE
    
    # draw the square
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')

if __name__ == '__main__':
    main()
```

```python
# rects and loops
from graphics import Canvas

def main():
    # make a canvas
    canvas = Canvas(300,300)

    # create 20 squares to show diagonal line
    for i in range(30):
        left_x = i*10
        top_y = i*10
        right_x = left_x + 10
        bottom_y = top_y + 10
        canvas.create_rectangle(left_x, top_y, right_x ,bottom_y,"blue")
        # keep track of i
        print(i)
   
if __name__ == '__main__':
    main()
```

# **5.18**  Lesson 8 : functions

```python
# call functions
function_name(input)

# define a function
def function_name(parameters):
    """explain the function"""
    ... # content
    ... # content
    return "result" # end the fuction and give back a value (feedback)

#  
```

> **argument** is the information that is given when we call it;
>
> **parameter** is the variable you name

```python
# draw a circle
from graphics import Canvas

# draw a japanese flag
circle(weight,height,color,center_weight,center_height,radius,circle_color)

# draw a bangladesh flag
circle(weight,height,color,center_weight,center_height,radius,circle_color)

def circle(weight,height,color,center_weight,center_height,radius,circle_color):
    canvas = Canvas(weight,height,color)
    canvas.create_oval(center_weight-radius, center_height-radius, center_weight+radius, center_height+radius, circle_color)
```

```python
# teacher's method
from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_japan_flag(canvas)
    canvas.wait_for_click()
    
    draw_bangladesh_flag(canvas)
    canvas.wait_for_click()
    
    draw_pulau_flag(canvas)
    canvas.wait_for_click()
    
    draw_georgia_flag(canvas)
 

def draw_japan_flag(canvas):
    draw_circle(canvas, CANVAS_WIDTH/2, CANVAS_HEIGHT/2, 120, 'red')

    
def draw_bangladesh_flag(canvas):
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, 'darkgreen')
    draw_circle(canvas, CANVAS_WIDTH * 0.4, CANVAS_HEIGHT / 2, 150, 'red')

    
def draw_pulau_flag(canvas):
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, 'dodgerblue')
    draw_circle(canvas, CANVAS_WIDTH * 0.4, CANVAS_HEIGHT / 2, 150, 'yellow')


def draw_circle(canvas, center_x, center_y, size, color):
    """
    draw a circle on the given canvas. Centered at the given location, in
    the given color
    """
    left_x = center_x - size/2
    top_y = center_y - size/2
    right_x = left_x + size
    bottom_y = top_y + size
    canvas.create_oval(left_x, top_y, right_x, bottom_y, color)

    
def draw_georgia_flag(canvas):
    canvas.clear()
    # some calculations for where the pluses go!
    x_left = CANVAS_WIDTH * 1/4
    x_right = CANVAS_WIDTH * 3/4
    y_top = CANVAS_HEIGHT * 1/4
    y_bottom = CANVAS_HEIGHT * 3/4
    
    # four calls to draw_plus
    draw_plus(canvas, x_left - 20, y_top - 20, x_left+20, y_top+20, 10)
    draw_plus(canvas, x_right - 20, y_top - 20, x_right+20, y_top+20, 10)
    draw_plus(canvas, x_left - 20, y_bottom - 20, x_left+20, y_bottom+20, 10)
    draw_plus(canvas, x_right - 20, y_bottom - 20, x_right+20, y_bottom+20, 10)
    
    # big background plus
    draw_plus(canvas, 0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, 30)
    
    
def draw_plus(canvas, x_1, y_1, x_2, y_2, width):
    """
    Draws a plus which is inscribed in the rectangle defined by the two 
    points (x_1, y_1) and (x_2, y_2). The thickness of each arm of the plus
    is also passed in as a parameter
    """
    # compute the middle of the plus
    mid_x = x_1 + (x_2 - x_1) / 2
    mid_y = y_1 + (y_2 - y_1) / 2
    
    # half an arm thickness
    half = width/2
    
    # create the two rectangles
    canvas.create_rectangle(x_1, mid_y - half, x_2, mid_y + half, 'red')
    canvas.create_rectangle(mid_x - half, y_1, mid_x + half, y_2, 'red')
    
       
if __name__ == '__main__':
    main()
```

```python
# chessboard
from graphics import Canvas
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = CANVAS_WIDTH
N_ROWS = 8
N_COLS = N_ROWS
SIZE = CANVAS_WIDTH / N_ROWS

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for r in range(N_ROWS):
        for c in range(N_COLS):
            draw_square(canvas, r, c)
            
def draw_square(canvas, r, c):
    print(r, c)
    color = get_color(r, c)
    x = c * SIZE
    y = r * SIZE
    end_x = x + SIZE
    end_y = y + SIZE
    
    canvas.create_rectangle(x, y, end_x, end_y, color, 'black')
            
        
def get_color(r, c):
    if is_even(r+c):
        return "green"
    else:
        return "beige"
'''def get_color(r, c):
    if is_even(r+c):
        return "black"
    else:
        return "white"'''
        
def is_even(value):
    return value % 2 == 0
            
if __name__ == '__main__':
    main()
```

# code11 :  Khansole Academy 

>In Code in Place we are all about building technology to help folks learn. Now it is your turn. Implement Khansole Academy—a program that helps other people learn addition! Write a program that randomly generates a simple addition problem for the user, reads in the answer from the user, and then checks to see if they got it right or wrong.
>
>More specifically, your program should be able to generate simple addition problems that involve adding two 2-digit integers (i.e., the numbers 10 through 99). The user should be asked for an answer to the generated problem. Your program should determine if the answer was correct or not, and give the user an appropriate message to let them know.
>
>A sample run of the program is shown below:
>
>```
>Khansole Academy
>What is 51 + 79? 
>Your answer: 120 
>Incorrect. 
>The expected answer is 130
>```
>
>Here's another sample run, where the user gets the question correct:
>
>```
>Khansole Academy
>What is 55 + 11? 
>Your answer: 66 
>Correct!
>```
>
>### Optional Extension
>
>If you're up for it, we can make Khansole Academy an even better learning tool. Be creative! We recommend you start with the "three in a row" extension first, then come up with your own :-).
>
>**Three in a row**
>
>In the previous milestone you wrote code to randomly generate one addition problem at a time and tell the user if they got it right or not. In this milestone, you should randomly generate addition problems *until the user has gotten 3 problems correct in a row*. (Note: the number of problems the user needs to get correctly in a row to complete the program is just one example of a good place to specify a constant in your program).
>
>You should be able to use a lot of your code from the previous milestone to help out here!
>
>A sample run of the program is shown below (user input is in bold italics).
>
>```
>Khansole Academy
>What is 51 + 79? 
>Your answer: 120 
>Incorrect. 
>The expected answer is 130 
>
>What is 33 + 19? 
>Your answer: 42 
>Incorrect. The expected answer is 52 
>
>What is 55 + 11? 
>Your answer: 66 
>Correct! You've gotten 1 correct in a row. 
>
>What is 84 + 25? 
>Your answer: 109 Correct! You've gotten 2 correct in a row. 
>
>What is 26 + 58? 
>Your answer: 74 Incorrect. 
>The expected answer is 84 
>
>What is 98 + 85? 
>Your answer: 183 Correct! 
>You've gotten 1 correct in a row. 
>
>What is 79 + 66? 
>Your answer: 145 Correct! You've gotten 2 correct in a row. 
>
>What is 97 + 20? 
>Your answer: 117 Correct! You've gotten 3 correct in a row. 
>
>Congratulations! You mastered addition.
>```

```python
import random

def main():
    print("Khansole Academy")
    # TODO: your code here
    # TODO: get the random numbers and get the rihgt addition
    loop = True
    i = 0
    while loop:
        first_number = random.randint(10,99)
        second_number = random.randint(10,99)
        right_result = first_number+second_number
        # TODO: ask the user the result and print the answer
        print(f"What is {first_number} + {second_number}?")
        ask =int(input("Your answer: "))
        # TODO: check if the answer is right and count the correct times 
        if ask == right_result:
            print("Correct!")
            i+=1
            print(f"You've gotten {i} correct in a row.")
            if i >= 3:
                loop = False
        else:
            print(f"Incorrect.\nThe expected answer is {right_answer}")

if __name__ == '__main__':
    main()
```

# code12 : Draw Flag

> Students in Code in Place are from 150 different countries! Wow. Let's celebrate our international class by drawing flags. To start out, one of the most straightforward flags to draw using python graphics is the flag of Indonesia:
>
> The dimensions of your flag should be based off the provided constants:
>
> ```
> # The width of the canvas
> CANVAS_WIDTH = 450
> # The height of the canvas
> CANVAS_HEIGHT = 300
> ```
>
> To draw the Indonesian flag all you need to do is to draw a single red rectangle which covers the top half of the graphics canvas. You don't need to draw the white stripe, the canvas is white by default.
>
> Once you have drawn the Indonesian flag, feel free to get creative. Consider making up your own flag!

```python
from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO, your code here
    canvas.create_rectangle(0,0,CANVAS_WIDTH, CANVAS_HEIGHT/2,"red")

if __name__ == '__main__':
    main()
```

# **5.26**  Lesson 9 : information flow



## reading : update functions



# code :  Quilt 

```python
'''A quilt, as you may know, is a blanket often composed of repeating "patches".Each patch has height and width of 100 pixels, given by the constant PATCH_SIZE. There are two different patch patterns that repeat in different locations.'''


from graphics import Canvas

# each patch is a square with this width and height:
PATCH_SIZE = 100
CANVAS_WIDTH = PATCH_SIZE * 4
CANVAS_HEIGHT = PATCH_SIZE * 2

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # draw the first row of patches
    draw_square_patch(canvas, 0, 0)
    draw_circle_patch(canvas, PATCH_SIZE, 0)
    draw_square_patch(canvas, PATCH_SIZE*2, 0)
    draw_circle_patch(canvas, PATCH_SIZE*3, 0)
    # TODO: your code here
    draw_circle_patch(canvas, 0, PATCH_SIZE)
    draw_square_patch(canvas, PATCH_SIZE, PATCH_SIZE)
    draw_circle_patch(canvas, PATCH_SIZE*2, PATCH_SIZE)
    draw_square_patch(canvas, PATCH_SIZE*3, PATCH_SIZE)
    
def draw_circle_patch(canvas, start_x, start_y):
    # TODO: your code here
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    canvas.create_rectangle(start_x, start_y, end_x, end_y, 'white')
    canvas.create_oval(start_x, start_y, 
        end_x, end_y, 'pink')

def draw_square_patch(canvas, start_x, start_y):
    # draws a purple frame at (start_x, start_y)
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    inset = 20
    # first draw a purple square over the entire patch
    canvas.create_rectangle(start_x, start_y, end_x, end_y, 'purple')
    # then draw a smaller white square on top
    canvas.create_rectangle(start_x+inset, start_y+inset, 
        end_x-inset, end_y-inset, 'white')
    
if __name__ == '__main__':
    main()
```

# **5.26**  Lesson 10 : animation

## animated square

```python
from graphics import Canvas
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SQUARE_SIZE = 40
VELOCITY = 2
DELAY = 0.01
# move to center
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    start_x = 0
    start_y = CANVAS_HEIGHT / 2 - SQUARE_SIZE / 2
    square = canvas.create_rectangle(start_x, start_y,
                    SQUARE_SIZE,
                    start_y + SQUARE_SIZE)  
	# animation loop
    while (start_x + SQUARE_SIZE / 2) < (CANVAS_WIDTH / 2):
            start_x += VELOCITY
            print("x:", start_x)
            canvas.moveto(square, start_x, start_y)
            time.sleep(DELAY)
            
	print("Done!")

if __name__ == '__main__':
	main()
```



## bouncing ball

```python
from graphics import Canvas
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 450
BALL_DIAMETER = 30
INITIAL_VELOCITY = 5
START_X = 0
START_Y = 0
DELAY = 0.001

def main():
    # create the canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # set the velocity of ball
    x_velocity = INITIAL_VELOCITY
    y_velocity = INITIAL_VELOCITY
    # set the ball's primitive position
    ball_x = START_X
    ball_y = START_Y
    # create the ball
    ball = canvas.create_oval(ball_x, ball_y,
                              ball_x + BALL_DIAMETER,
                              ball_y + BALL_DIAMETER,
                              'blue')
    # set the rules of ball movement
    while True:
        if (ball_x < 0) or (ball_x + BALL_DIAMETER >= CANVAS_WIDTH):
            x_velocity = -x_velocity
        if (ball_y < 0) or (ball_y + BALL_DIAMETER >= CANVAS_HEIGHT):
            y_velocity = -y_velocity
        # set the ball's position after moving
        ball_x += x_velocity
        ball_y += y_velocity
        canvas.moveto(ball, ball_x, ball_y)
        time.sleep(DELAY)

if __name__ == '__main__':
    main()
```



## graphics function

```python
# get the x and y location of the mouse
mouse_x = canvas.get_mouse_x()
mouse_y = canvas.get_mouse_y()

# move shape to some new coordinates
canvas.moveto(shape, new_x, new_y)

# move shape by a given change_x and change_y
canvas.move(shape, change_x, change_y)

# get the coordinates of a shape
top_y = canvas.get_top_y(shape)
left_x = canvas.get_left_x(shape)

# return a list of elements in a rectangle area
results = canvas.find_overlapping(left_x, top_t, right_x, bottom_y)
```



## mouse tracker

```python
# Mouse Tracker
from graphics import Canvas
import time

CANVAS_SIZE = 400
PAUSE_TIME = 1/50

def main():
    canvas = Canvas(CANVAS_SIZE, CANVAS_SIZE)
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        time.sleep(PAUSE_TIME)
        print("Mouse location: (" + str(mouse_x) + ", " + str(mouse_y) + ")")

if __name__ == '__main__':
    main() 
```

# **diagnostics**

```python
# 1.asks the user for their height in meters and prints whether or not they are the correct height to be a NASA astronaut.
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
```

```python
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
```

```PYTHON
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
```

```PYTHON
'''A simple way to achieve great things in life is to make small forward progress every day. Non-decreasing progress is one of the principles behind modern AI.

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
```

```PYTHON
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
  
'''Fix this program so that it does what it is meant to. You can make changes to both draw_car and main, but draw_car must implement the functionality described in its comment. Write a comments for each line you changed.

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
```

# **6.2**  Lesson 11 : lists

variables have limitations

what is a data structure?

## grammer of list

```python
# updating elements in a list
names = ["A","B","C"] 
names[2] = D

# getting the number of element
num_names = len(names)

# doubling a list
numbers = [1,2,3,4,5]
for i in range(len(numbers)):
    ele_at_index = numbers[i]
    numbers[i] = 2 * ele_at_index
    print(numbers)

# list operation
# adding to the end of a list
my_list.append(42)
# add to the list
another = [1,2,3]
my_list.extend(another)
combine = my_list + another # another way
# removing an element from the end of the list
my_list.pop()
my_list.pop(1) # remove the my_list[1]
# removing an element from the list
my_list.remove(42) # from the beginning to the end

# does an element in a list?
my_list = [42,100,10]
if 42 in my_list:
    print("List has this element!")
else:
	print("Element is not in the list!")

# for loop
number = [1,2,3,4,5,6]
for ele in number:
    print(ele)
    
# is a list is empty?
my_list = [42]
if my_list:
    print("List has elements1!")
else:
    print("List is empty!")
    
# get the index of a certain number
list = [42,100,10]
idx = list.index(100) # 1

# insert an element to the position of the index and shift the others down
list.insert(1,27) # [42,27,100,10]

# functions of lists
max(list)
min(list)
sum(list)
```

## memory model

we can not modify the value of an immutable of variable, except by setting it equal to a new value

lists and most other data structure are mutable, we can modify the value of a a list without creating a new one

## canvas eraser 

```python
"""
This program implements an 'eraser' on a canvas. 

The canvas consists of a grid of blue 'cells' which are drawn 
as rectangles on the screen. We then create an eraser rectangle
which, when dragged around the canvas, sets all of the rectangles 
it is in contact with to white.
"""

from graphics import Canvas
import time
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()
    
    left_x = mouse_x
    top_y = mouse_y
    
    right_x = mouse_x + ERASER_SIZE
    bottom_y = mouse_y + ERASER_SIZE
    
    overlapping_objects = canvas.find_overlapping(left_x,top_y,right_x,bottom_y)
    
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            canvas.set_color(overlapping_object,"white")


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    num_rows = CANVAS_HEIGHT // CELL_SIZE  # figure out how many rows of cells we need
    num_cols = CANVAS_WIDTH // CELL_SIZE   # figure out how many columns of cells we needd
    
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE   # The right coordinate of the cell is CELL_SIZE pixels away from the left
            bottom_y = top_y + CELL_SIZE   # The bottom coordinate of the cell is CELL_SIZE pixels away from the top
            
            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
            
            
    canvas.wait_for_click()  # wait for the user to click before creating the eraser
    
    last_click_x, last_click_y = canvas.get_last_click()
    
    eraser = canvas.create_rectangle(
        last_click_x, 
        last_click_y, 
        last_click_x + ERASER_SIZE, 
        last_click_y + ERASER_SIZE, 
        'pink'
    )
    
    while True:
        # move the eraser, and erase what it's touching
        
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        
        erase_objects(canvas, eraser)  # we need to implement this!
        
        time.sleep(0.05)
        

if __name__ == '__main__':
    main()
```

# **6.2**  Lesson 12 : dictionaries

**what are dictionaries in python?**

associate a key with a value

key : an unique indentifier

```python
dictionary = {"A":"a","B":"b"}
empty = {}

# accessing elements of dictionaries
dictionary['A'] # a
"A" in dictionary # True

# add elements in a dictionary
dictionary['C'] = 'c'  # {"A":"a","B":"b","C":"c"}

# LOOP OVER A DICTIONARY
for key in ages:
    value = ages[key]
    print(str(key) + " -> " + str(value))
    
# a range of keys : dict.keys()
for key in ages.keys():
     print(str(key) + " -> " + str(ages[key]))
list(ages.keys)  # ["Chris","Juliette","Mehran"]

# a range of values : dict.values()
for value in ages.values():
     print(value)
list(ages.values)  # [32,24,50]

# a range of elemen
for key, value in ages.items():
     print(str(key) + " -> " + str(value))

# remove key_value pair with the given key. return value from the pair : dict.pop(key)
ages.pop('Mehran') # 50
# remove key_value pair with the given key. return nothing : del dict[key]
del ages["Mehran"]

# remove all the pair in the dictionary : dict.clear()
ages.clear()

# the number of the pair
len(dict)
```

## lists VS dictionaries

# code : count nums

```python
"""
File: count_words.py
--------------------
This program counts the number of times each number appears in a list of numbers.
"""


def get_user_numbers():
    """
    Create an empty list.
    Ask the user to input numbers and store them in a list. 
    Once they enter a blank line, break out of the loop and return the list.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        
        # If the user enters a blank line, break out of the loop and stop asking for input
        if user_input == "":
            break
        
        # convert the user input to an integer and add it to the list
        num = int(user_input)
        user_numbers.append(num)
    
    return user_numbers

def count_nums(num_lst):
    """
    Create an empty dictionary.
    Loop over the list of numbers. 
    If the number is not in the dictionary, add it as a key with a value of 1.
    If the number is in the dictionary, increment its value by 1.
    """
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    return num_dict


def print_counts(num_dict):
    """
    Loop over the dictionary and print out each key and its value.
    """
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")


def main():
    """
    Ask the user to input numbers and store them in a list. Once they enter a blank line,
    print out the number of times each number appeared in the list.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)


# Python boilerplate.
if __name__ == '__main__':
    main()
```

# code : phonebook

```python
"""
File: phonebook.py
------------------
Program to show an example of using dictionaries to maintain
a phonebook.
"""


def read_phone_numbers():
    """
    Ask the user for names/numbers to story in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}                   # Create empty phonebook

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


# Python boilerplate.
if __name__ == '__main__':
    main()
```

# code14 : BabySnake

>In this assignment we are going to make a baby version of the classic Atari game of Snake. It was famously shipped on the original Apple II computers as well as Nokia phones. Here is a demo with a few extensions: Baby Snake Demo  
>
>**Milestone #1: Set up the World**
>
>Draw the following world! It has a blue square is the "player" the red square is the "goal". The player and the goal are both 20 pixels by 20 pixels. 
>
>The player should start in the top left corner of the world. You can place the goal anywhere you like as long as its x and y values are both multiplies of 20. Here is a reasonable configuration where the goal is at (360, 360)
>
>**Milestone #2: Animate**
>
>Each time through the animation loop you should move your player 20 pixels (this size of the player) in the direction it is traveling. The directions are either left, right, up or down. At the start the player should be traveling to the right
>
>**Milestone #3: Handle Key Press**
>
>the direction that the player is traveling can either be Left, Right, Up or Down and should be controlled by the keyboard. 
>
>We haven't seen the keyboard in Code in Place. It works just like the mouse! At any point in a graphics program you can ask the canvas for the last key press 
>
>```
>key = canvas.get_last_key_press()
>```
>
>The key variable will then hold the *name* of the key which was last pressed (or None if no key has been pressed). If the name of the key is "ArrowLeft" that means the last key the user pressed was the left arrow. Here is an example of printing arrow keys:
>
>```
>key = canvas.get_last_key_press()
>if key == 'ArrowLeft':
>    print('left arrow pressed!')
>if key == 'ArrowRight':
>    print('right arrow pressed!')
>if key == 'ArrowUp':
>    print('up arrow pressed!')
>if key == 'ArrowDown':
>    print('down arrow pressed!')
>```
>
>You should process canvas.get_last_key_press() inside the animation loop. We strongly encourage you to keep a variable which stores the current direction of travel.
>
>**Milestone #4: Detecting collisions**
>
>If the player goes out of bounds, the game is over. Write code that checks for, and handles, out of bounds cases. You will likely benefit from using:
>
>```
>x = canvas.get_left_x(obj)
>y = canvas.get_top_y(obj)
>```
>
>where the obj parameter can be either the player variable, or the goal variable. The return type is always an integer, so you can compare the value of say the player x and the goal x.
>
>**Milestone #5: Moving the goal**
>
>When the player hits the goal, you should randomly move the goal to a new location, anywhere on the board. Write code that detects if the user has hit the goal, and randomly places the goal in a new location. You will need to use the randint function which returns an integer in the given range:
>
>```
>random.randint(0, max_value)
>```
>
>Recall that the new x and y of the goal should be multiples of 20, otherwise it may be hard to detect if the player and the goal touch. There are many algorithms which you could come up with to get a random value which is a multiple of 20. Also recall that randint is inclusive, which means it can return 0 and it can also return max_value. 
>
>**Extensions**
>
>You did it! Congratulations, that was a huge program. If you want to keep going, awesome. Add any extension you like. Here are a few that we think are fun:
>
>1. Get faster each time the player touches the goal.
>2. Keep track of points
>3. Add obstacles
>
>**Full Snake?**
>
>If you are feeling very adventurous you could try and implement the full game of snake. Here is a link to an online version: https://playsnake.org/. The full game of snake is a hard challenge even for a well seasoned programmer. If you do go down this path, here are a few pro tips:
>
>- Program your snake in a new project (leave this one as baby snake)
>- Represent your snake using a list of rectangles (where the rectangles are the shapes returned by create_rect). This will make it much easier to move your snake. You will only need to change the head and the tail.
>- Us the find_overlapping function to tell if you have hit yourself.

