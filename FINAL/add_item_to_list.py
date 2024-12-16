# Name: Thomas Caine
# Date: 12/16/24
# Program description: This program will ask for the user to input the full filename of a list followed by an item to add. 

def add_item_to_list(file_name):
    
    file_name = input(f'Please type in the name of a stickynotez: ')

    if file_name == 'grocery.txt':
        file = open('grocery.txt', 'a')
        new_name = input('What would you like to add to this list? ')
        file.write(new_name + '\n')
        file.close()
        print() 

    elif file_name == 'movies.txt':
        file = open('movies.txt', 'a')
        new_name = input('What would you like to add to this list? ')
        file.write(new_name + '\n')
        file.close()
        print()

    elif file_name == 'palindrome.txt':
        file = open('palindrome.txt', 'a')
        new_name = input('What would you like to add to this list? ')
        file.write(new_name + '\n')
        file.close()
        print()

add_item_to_list('file_name')
