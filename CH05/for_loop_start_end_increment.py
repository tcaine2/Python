# FILE NAME - for_loop_start_end_increment.py


# NAME: Thomas Caine
# DATE: 10/21/24
# BRIEF DESCRIPTION: THis program covers what was talked about in the for-loop video 
# but will go one step further and ask the user to pick a number to go up by and then 
# display all the numbers on one line.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########

# You must create a main() function that calls your function 
# that runs the loop.

# You also have to make a call to main() in the program.

def main():
    for_loop_start_end_increment()

def for_loop_start_end_increment():
    start_value = int(input('Starting point: '))
    end_value = int(input('Ending point: '))
    increment_value = int(input('Increment by: '))

    for number in range(start_value, end_value + 1, increment_value):
        print(number, ' ', end='')

main()

########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Starting point: 3
Ending point: 12
Increment by: 4
3 7 11 
'''


'''
Starting point: 12
Ending point: 22
Increment by: 3
12 15 18 21 
'''


'''
Starting point: 60
Ending point: 10
Increment by: -4
60 56 52 48 44 40 36 32 28 24 20 16 12 
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