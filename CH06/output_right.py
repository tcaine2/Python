# FILE NAME - output_right.py

# NAME: 
# DATE: 
# BRIEF DESCRIPTION:  




def main():
    output_right()

def output_right():
    # Declare an array called `park_visitors`.
    guests = []

    # Declare a variable called `guest_name` and set it equal to ''.
    guest_name = ''

    # Collect information from the user. The user can keep entering 
    # names of guests as they enter the line for the attraction.
    # Once the last guest is loaded into the list, the DMV employee will
    # type 'EOF' (which in computer nerdom translates to "End of File").
    while guest_name != 'EOF':
        guest_name = input('Enter the name of the guest: ')

        # Need to ensure that "EOF" is not input into the system as a name!
        if guest_name != 'EOF':
            guests.append(guest_name)

    print()

    # Output the names
    print(guests)

    
    
    #########################################
    #               YOUR JOB:               #
    #                                       #
    # 1. Move the last item in the list to  #
    #    be the first item                  #
    #                                       #
    #########################################

    ########## ENTER YER CODE BELOW THIS LINE ##########

    if guests:
        first_customer = guests.pop(0)
        guests.append(first_customer)

    print(guests)

    ########### END YER CODE ABOVE THIS LINE ###########

    
main()





########################################
#          SAMPLE OUTPUT
########################################

'''
Enter the name of the guest: Alice
Enter the name of the guest: Bob
Enter the name of the guest: Charlie
Enter the name of the guest: Danielle
Enter the name of the guest: EOF

['Alice', 'Bob', 'Charlie', 'Danielle']
['Danielle', 'Alice', 'Bob', 'Charlie']
'''


'''
Enter the name of the guest: Eliza
Enter the name of the guest: EOF

['Eliza']
['Eliza']
'''


'''
Enter the name of the guest: 1234
Enter the name of the guest: 2345
Enter the name of the guest: 3456
Enter the name of the guest: 4567
Enter the name of the guest: EOF

['1234', '2345', '3456', '4567']
['4567', '1234', '2345', '3456']
'''




########################################
#          REFLECTION QUESTIONS
########################################

'''

1. How did you move the element in the list this time?







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