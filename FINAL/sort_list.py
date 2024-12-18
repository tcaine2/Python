# Name: Thomas Caine
# Date: 12/18/24
# Program description: This program will ask for the user to input the full filename of a list.

def sort_list(filename):
    
    if filename == 'grocery.txt':
        # Create an empty list
        list_words = []
        # Open the file (passed in with the variable name `filename`)
        # Iterate through the list and append each item to the empty list that was just created
        existing_text_list = open('grocery.txt', 'r')
        for line in existing_text_list:
            list_words.append(line.strip())
        # Close the file
        existing_text_list.close()
        # Use the .sort() function to sort the list
        list_words.sort()
        # Open the same file, this time with the ability to overwrite the contents
        # Iterate through the list and write each item to the file
        existing_text_list = open('grocery.txt', 'r')
        for line in existing_text_list:
            list_words.insert(2, line)
        # Close the file
        existing_text_list.close()
        # Open the file and print out the contents
        existing_text_list = open('grocery.txt', 'r')
        print('SORTED LIST: \n')
        print(sort_list('filename'))
    
    elif filename == 'movies.txt':
        list_words = []
        existing_text_list = open('movies.txt', 'r')
        for line in filename:
            list_words.append(line.strip())
        existing_text_list.close()
        list_words.sort()
        existing_text_list = open('movies.txt', 'r')
        for line in filename:
            list_words.insert(2, line)
        existing_text_list.close()
        filename = open('movies.txt', 'r')
        print('SORTED LIST: \n')
        print(sort_list('filename'))

    elif filename == 'palindrome.txt':
        list_words = []
        existing_text_list = open('movies.txt', 'r')
        for line in filename:
            list_words.append(line.strip())
        existing_text_list.close()
        list_words.sort()
        existing_text_list = open('palindrome.txt', 'r')
        for line in filename:
            list_words.insert(2, line)
        existing_text_list.close()
        filename = open('palindrome.txt', 'r')
        print('SORTED LIST: \n')
        print(sort_list('filename'))
        
sort_list('filename')
    
def main():
    file_choice = input('Please type in the name of a stickynotez: ')
    sort_list(file_choice)

main()
