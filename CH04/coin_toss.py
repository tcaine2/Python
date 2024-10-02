# FILE NAME - coin_toss.py

# NAME: Thomas Caine
# DATE: 10/2/24
# BRIEF DESCRIPTION: This lab will randomly return Heads or Tails



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



import random

def main():
    coin_toss()

def coin_toss():
    #print('===== Coin Flipper =====')
    
    ########## ENTER YER CODE BELOW THIS LINE ##########

    import random

flip_input = random.randint(0,100)

print('===== Coin Flipper =====')

if flip_input > 51:
    print('Heads')
else:
    print('Tails')

    ########### END YER CODE ABOVE THIS LINE ###########    


main()




########################################
#          SAMPLE OUTPUT
########################################

'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 

For some reason the portion that said "Coin toss" was outputting twice and I had to comment it out above where my code goes in





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