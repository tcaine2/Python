# Name: Thomas Caine
# Date: 12/16/24
# Program description: This program will ask for the user to input the full filename of a list and will then output the results. 

def output_file_contents(file_name):
    
    file_name = input(f'Please type in the name of a stickynotez: ')
    if(file_name == 'grocery.txt'):
        file = open('grocery.txt', 'r')
        for line in file:
            print(line, end="")
        print() 
    if(file_name == 'movies.txt'):
        file = open('movies.txt', 'r')
        for line in file:
            print(line, end="")
        print() 
    if(file_name == 'palindrome.txt'):
        file = open('palindrome.txt', 'r')
        for line in file:
            print(line, end="")
        print() 

output_file_contents('file_name')