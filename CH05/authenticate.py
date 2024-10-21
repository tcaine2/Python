# FILE NAME - authenticate.py

# NAME: Thomas Caine
# DATE: 10/21/24
# BRIEF DESCRIPTION:  In this lab, the user keeps typing in a password until they get it right.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########

# You must create a main() function that calls your function 
# that runs the loop.

# You also have to make a call to main() in the program.

def main():
    authenticate()

def authenticate():
    tries = 0
    password = 'tooManySecrets'  # The correct password

    while True:
        number_input = input('Enter password: ')  # Read input as a string
        tries += 1

        if number_input == password:
            print('Access granted.')
            break
        else:
            print('Password does not match.')

main()

########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Enter password: a

Password does not match.
Enter password: b

Password does not match.
Enter password: tooManySecrets

Access granted.
'''


'''
Enter password: tooManySecrets

Access granted.
'''


'''
Enter password: toomanysecrets

Password does not match.
Enter password: TOOMANYSECRETS

Password does not match.
Enter password: too_Many_Secrets

Password does not match.
Enter password: tooManySecrets

Access granted.
'''



########################################
#            ATTESTATION
########################################

'''

Please gauge your utilization of AI on the following spectrum. Place an "X" in front
of the appropriate response. Only choose one of the following:

[ ] I did not use AI at all for this lab.
[ ] I wrote the initial draft of the software but had AI help me make it better.
[ ] I fed the lab description to AI and had it generate a response but I modified it.
[ ] AI created the entire program for me.



It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[ ] I'm solid. Totally got it.

'''