# FILE NAME - compliment2.py

# NAME: Thomas Caine
# DATE: 10/2/24
# BRIEF DESCRIPTION:  Building off of compliment.py, this program goes a step further and will have custom output for yes as well as not yes



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience




def main():
    compliment()

def compliment():

    ########## ENTER YER CODE BELOW THIS LINE ##########

    user_input = input('Would you like a compliment? ')

    if user_input == 'yes':
        print('You have wonderful eyes.')
        print('Thank you for playing.')
    else:
        print('No compliment for you!')
        print('Thank you for playing.')

    ########### END YER CODE ABOVE THIS LINE ###########

main()

########################################
#          SAMPLE OUTPUT
########################################

'''
Would you like a compliment? yes
You have wonderful eyes.
Thank you for playing.
'''


'''
Would you like a compliment? Yes
No compliment for you!
Thank you for playing.
'''


'''
Would you like a compliment? y
No compliment for you!
Thank you for playing.
'''


'''
Would you like a compliment? no
No compliment for you!
Thank you for playing.
'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 

Making sure the output had all the correct punctuation





'''



########################################
#            ATTESTATION
########################################

'''

Please gauge your utilization of AI on the following spectrum. Place an "X" in front
of the appropriate response. Only choose one of the following:

[ X ] I did not use AI at all for this lab.
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
[ X ] I'm solid. Totally got it.

'''