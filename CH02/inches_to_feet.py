# FILE NAME - inches_to_feet.py

# NAME: Thomas Caine
# DATE: 9/18/24
# BRIEF DESCRIPTION:  This is a program  that will ask the user for a number 
# of total inches. Then convert the total inches into feet and inches. 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience



def main():
    convert()



def convert():

    # BEWARE! You'll need to cast not only the input from the user
    # but also maybe the number of feet

    ########## ENTER YER CODE BELOW THIS LINE ##########
    
    inches_input = int(input("Enter the number of inches: "))
    feet = inches_input // 12
    remaining_inches = inches_input % 12
    print(f"{inches_input} inches is {feet} feet, and {remaining_inches} inches")
       
    ########### END YER CODE ABOVE THIS LINE ###########

main()



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter the number of inches: 14

14 inches is 1 feet, and 2 inches


'''



'''

Enter the number of inches: 100

100 inches is 8 feet, and 4 inches

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does it mean to "cast" input from the user?


In Python casting refers to converting a value from one data type to another. 
When you "cast" user input, you transform the input into another type, such as str, int or float



'''
