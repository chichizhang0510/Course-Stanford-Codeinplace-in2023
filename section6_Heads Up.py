import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'

def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    f = open(FILE_NAME)
    lines = []
    for line in f:
        # removes whitespace characters (\n) from the start and end of the line
        line = line.strip() 
        # if the line was only whitespace characters, skip it 
        if line != "":
            lines.append(line)
    return lines


def main():
    # your code here :) 
    loop = True
    while loop:
        lines = get_words_from_file()
        # print(get_words_from_file())
        head_number = random.choice(lines)
        print(head_number)
        user = input("")
        # if user == "exit":
        #     loop = False
    

if __name__ == '__main__':
    main()
    
    
    
-------------------- leader's code --------------------------------
import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'

def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    f = open(FILE_NAME)
    lines = []
    for line in f:
        # removes whitespace characters (\n) from the start and end of the line
        line = line.strip() 
        # if the line was only whitespace characters, skip it 
        if line != "":
            lines.append(line)
    return lines

def play_game(words):
    while True:
        random_word = random.choice(words)
        input(random_word)

def main():
    words = get_words_from_file()
    play_game(words)

if __name__ == '__main__':
    main()
