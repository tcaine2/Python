# FILE NAME - output_values.py

# NAME: Thomas Caine
# DATE: 10/16/24
# BRIEF DESCRIPTION: For this lab the user will get to enter five numbers. The program will then sort the list and output the numbers



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience




def main():
    output_values()

def output_values():
    # Create an empty list
    
    numbers =[]



    # Walk through the list and grab a number from the
    # user. Insert that number into the next available cell

    #########################################
    #               YOUR JOB:               #
    #                                       #
    # 1. Sort the list                      #
    # 2. Print out the list naturally       #
    # 3. Print out the list in a pretty way #
    #                                       #
    #########################################

    ########## ENTER YER CODE BELOW THIS LINE ##########


    # Sort the list
    for x in range(5):
        numbers.append(int(input('Enter a number: ')))

    print()

    # Print out the list naturally:
    print(f'[{numbers[0]}, {numbers[1]}, {numbers[2]}, {numbers[3]}, {numbers[4]}]')

    # Print out the list in a pretty way:
    print(f'Your numbers are: {numbers[0]} {numbers[1]} {numbers[2]} {numbers[3]} {numbers[4]}')


    ########### END YER CODE ABOVE THIS LINE ###########


main()





########################################
#          SAMPLE OUTPUT
########################################

'''
Enter a number: 5
Enter a number: 4
Enter a number: 6
Enter a number: 34
Enter a number: 43

[4, 5, 6, 34, 43]
Your numbers are: 4  5  6  34  43 
'''


'''
Enter a number: 100
Enter a number: 99
Enter a number: 98
Enter a number: 9
Enter a number: 97

[9, 97, 98, 99, 100]
Your numbers are: 9  97  98  99  100
'''


'''
Enter a number: 0
Enter a number: 0
Enter a number: -1
Enter a number: 1
Enter a number: 0

[-1, 0, 0, 0, 1]
Your numbers are: -1  0  0  0  1  
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?

using f-strings can be helpful when you want to output certain characters as text such as [] and ,.





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