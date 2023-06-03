def main():
    # Create a list called `fruit_list` that contains the following fruits: 'apple', 'banana', 'orange', 'grape', 'pineapple'.
    fruit_lst = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list.
    lst_length = len(fruit_lst)
    print(lst_length)

    # Add 'mango' at the end of the list. 
    fruit_lst.append('mango')

    # Print the updated list.
    for fruit in fruit_lst:
        print(fruit)

if __name__ == '__main__':
    main()
