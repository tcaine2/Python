# FILE NAME - password.py

# NAME: Thomas Caine
# DATE: 10/7/24
# BRIEF DESCRIPTION: This program will take in a number from the user, seeds the random module with that input, 
# and then generates a random password using specific criterea



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



def main():
    generate_password()

def generate_password():

  
    ########## ENTER YER CODE BELOW THIS LINE ##########
    import random
    import string

    seed_value = int(input("Enter a seed value for the random number generation: "))
    random.seed(seed_value)

    special_chars = "!@#$&(),-_"
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    
    first_special = random.choice(special_chars)
    first_lower = random.choice(lowercase)
    first_upper = random.choice(uppercase)
    second_lower = random.choice(lowercase)
    second_upper = random.choice(uppercase)
    first_digit = random.choice(digits)
    second_digit = random.choice(digits)
    last_special = random.choice(special_chars)

    print(f'Your random password is: {first_special}{first_lower}{first_upper}{second_lower}{second_upper}{first_digit}{second_digit}{last_special}')

    ########### END YER CODE ABOVE THIS LINE ###########

main()



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a seed for the random number generation: 33
Your random password is:
_fUhI78-

'''



'''

Enter a seed for the random number generation: 22
Your random password is:
#hAtO21(

'''



'''

Enter a seed for the random number generation: 0
Your random password is:
)yNbI87)

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 
I couldnt come up with a good way to output the code once I determined how to get the correct characters to output so I used "+" and added all the 
variable's together at once.





2. What value do you see in the `string` module?
The string module lets you input sets of characters like ascii_lowercase, ascii_uppercase, and digits, 
which simplifies generating passwords or working with text, instead inputting "ABCDEF...." or "1234..."
manually into the code





'''



