def main():
    """
    You should write your code here. 
    """
    curr_value = int(input("Enter a number: "))
    loop = True
    while loop:
        curr_value = curr_value*2
        print(curr_value)
        if curr_value>=100:
            loop = False

if __name__ == '__main__':
    main()
