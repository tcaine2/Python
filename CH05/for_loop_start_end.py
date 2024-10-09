# FILE NAME - for_loop_start_end.py

# NAME: Thomas Caine
# DATE: 10/9/24
# BRIEF DESCRIPTION:  This program will ask the user to pick a starting point and ending point and then display all the numbers, inclusively on one line.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience






########## ENTER YER CODE BELOW THIS LINE ##########

# You must create a main() function that calls your function 
# that runs the loop.

# You also have to make a call to main() in the program.

def main():
    for_loop_start_end()

def for_loop_start_end():
    
    start_value = int(input('Starting point: '))
    end_value = int(input('Ending point: '))

    for number in range (start_value,end_value+1):
        print(number, ' ',end='')

main()

########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''
Starting point: 3
Ending point: 7
3 4 5 6 7
'''


'''
Starting point: -4
Ending point: 4
-4 -3 -2 -1 0 1 2 3 4
'''


'''
Starting point: 0
Ending point: 1
0 1
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