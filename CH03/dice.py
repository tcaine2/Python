# FILE NAME - dice.py

# NAME: Thomas Caine
# DATE: 09/25/24
# BRIEF DESCRIPTION:  This is a program that takes in a number from the user and  
# seeds the random module with that input, and then outputs the value of two 
# randomly rolled dice.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



def main():
    roll_die()

def roll_die():
    
  
    ########## ENTER YER CODE BELOW THIS LINE ##########

    import random

    dice_seed = int(input('Enter a seed for the random number generation: '))
    random.seed(dice_seed)

    dice_output_one = int(random.randint(1,6))
    dice_output_two = int(random.randint(1,6))
    
    print(f'Die roll one is {dice_output_one}')
    print(f'Die roll two is {dice_output_two}')






    ########### END YER CODE ABOVE THIS LINE ###########

main()



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
Die roll one is 5
Die roll two is 2

'''



'''

Enter a seed for the random number generation: 22
Die roll one is 2
Die roll two is 2

'''



'''

Enter a seed for the random number generation: -30
Die roll one is 5
Die roll two is 3

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is the purpose of "seeding" the random number generator?






'''



