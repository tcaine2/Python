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