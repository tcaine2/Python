# FILE NAME - while_loop_guess_high_low.py

# NAME: Thomas Caine
# DATE: 10/21/24
# BRIEF DESCRIPTION: This lab will continue from the previous one where there is now a feature which will 
# tell the user if their guess is too high or too low. 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience




SECRET_NUMBER = 33


########## ENTER YER CODE BELOW THIS LINE ##########

# You must create a main() function that calls your function 
# that runs the loop.

# You also have to make a call to main() in the program.

def main():
    while_loop_guess()

def while_loop_guess():
    tries = 0

    while True:
        number_input = int(input('Guess a number: '))
        tries += 1

        if number_input == SECRET_NUMBER:
            print(f'You guessed in {tries} tries.')
            break
        elif number_input < SECRET_NUMBER:
            print('Your guess is too low.')
        else:
            print('Your guess is too high.')

main()







########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Guess a number: 22
Your guess is too low.

Guess a number: 44
Your guess is too high.

Guess a number: 33

You guessed in 3 tries.
'''


'''
Guess a number: 33

You guessed in 1 tries.Guess a number: -9
Your guess is too low.

Guess a number: 100
Your guess is too high.

Guess a number: 30
Your guess is too low.

Guess a number: 32
Your guess is too low.

Guess a number: 34
Your guess is too high.

Guess a number: 33

You guessed in 6 tries.
'''


'''
Guess a number: -9
Your guess is too low.

Guess a number: 100
Your guess is too high.

Guess a number: 30
Your guess is too low.

Guess a number: 32
Your guess is too low.

Guess a number: 34
Your guess is too high.

Guess a number: 33

You guessed in 6 tries.
'''



########################################
#            ATTESTATION
########################################

'''

Please gauge your utilization of AI on the following spectrum. Place an "X" in front
of the appropriate response. Only choose one of the following:

[ ] I did not use AI at all for this lab.
[ X ] I wrote the initial draft of the software but had AI help me make it better.
[ ] I fed the lab description to AI and had it generate a response but I modified it.
[ ] AI created the entire program for me.



It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[ X ] I'm solid. Totally got it.

'''
