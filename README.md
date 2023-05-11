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

