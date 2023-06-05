'''find details of instruction from readme file'''

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
