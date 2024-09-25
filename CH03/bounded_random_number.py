# FILE NAME - bounded_random_number.py

# NAME: Thomas Caine
# DATE: 09/25/24
# BRIEF DESCRIPTION: This program will output a random number that takes in a number from the user and 
# seeds the random module with that input.


# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



def main():
    bounded_random()

def bounded_random():
    
  
    ########## ENTER YER CODE BELOW THIS LINE ##########

    import random

    bounded_seed_from_user = int(input('Enter a seed for the random number generation: '))
    random.seed(bounded_seed_from_user)

    random_number = int(random.randint(1,10))
    print(random_number)








    ########### END YER CODE ABOVE THIS LINE ###########

main()



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
10

'''



'''

Enter a seed for the random number generation: 32
2

'''



'''

Enter a seed for the random number generation: 100
3

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is a good way to remember if the arguments (parameters) for a bounded number are inclusive or exclusive?






'''



