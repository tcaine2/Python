# FILE NAME - rectangle_redux.py

# NAME: Thomas Caine
# DATE: 10/21/24
# BRIEF DESCRIPTION: This lab will build off the first rectangle lab but now 
# the user gets to pick a height. The software should always output the top and 
# the bottom of the rectangle, but the height depends on the user's input.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########

# You must create a main() function that calls your function 
# that runs the loop.

# You also have to make a call to main() in the program.

def main():
    height = int(input('How tall would you like the rectangle? '))
    draw_rectangle(height)

def draw_rectangle(height):
    width = 5

    print('*' * width)

    for _ in range(height - 2):
        print('*' + ' ' * (width - 2) + '*')

    if height > 1:
        print('*' * width)

main()

########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
How tall would you like the rectangle? 3
*****
*   *
*   *
*   *
*****
'''


'''
How tall would you like the rectangle? 1
*****
*   *
*****
'''


'''
How tall would you like the rectangle? 0
*****
*****
'''


'''
How tall would you like the rectangle? 10
*****
*   *
*   *
*   *
*   *
*   *
*   *
*   *
*   *
*   *
*   *
*****
'''


########################################
#            ATTESTATION
########################################

'''

Please gauge your utilization of AI on the following spectrum. Place an "X" in front
of the appropriate response. Only choose one of the following:

[ ] I did not use AI at all for this lab.
[ ] I wrote the initial draft of the software but had AI help me make it better.
[ X ] I fed the lab description to AI and had it generate a response but I modified it.
[ ] AI created the entire program for me.



It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ X ] I pretty much get it.
[ ] I'm solid. Totally got it.

'''