# FILE NAME - output_left.py

# NAME: Thomas Caine
# DATE: 10/30/24
# BRIEF DESCRIPTION: This code will be taking input from the user as they provide integers for a list. 
# When they are done, we will output all the elements in the list--in order--with one caveat: the first 
# item in the list will be output as the last item.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience




def main():
    output_left()

def output_left():
    # Declare an array called `customers`.
    customers = []

    # Declare a variable called `driver_name` and set it equal to ''.
    driver_name = ''

    # Collect information from the user. The user can keep entering 
    # names of drivers as they enter the DMV. Once the last driver
    # is loaded into the list, the DMV employee will type 'EOF' 
    # (which in computer nerdom translates to "End of File").
    while driver_name != 'EOF':
        driver_name = input('Enter the name of the customer: ')

        # Need to ensure that "EOF" is not input into the system as a name!
        if driver_name != 'EOF':
            customers.append(driver_name)

    print()

    # Output the names
    print(customers)

    
    
    #########################################
    #               YOUR JOB:               #
    #                                       #
    # 1. Move the first item in the list to #
    #    be the last item                   #
    #                                       #
    #########################################

    ########## ENTER YER CODE BELOW THIS LINE ##########

    if customers:
        first_customer = customers.pop(0)
        customers.append(first_customer)

    print(customers)

    ########### END YER CODE ABOVE THIS LINE ###########
    
    
main()



########################################
#          SAMPLE OUTPUT
########################################

'''
Enter the name of the customer: Alice
Enter the name of the customer: Bob
Enter the name of the customer: Charlie
Enter the name of the customer: Danielle
Enter the name of the customer: EOF

['Alice', 'Bob', 'Charlie', 'Danielle']
['Bob', 'Charlie', 'Danielle', 'Alice']
'''


'''
Enter the name of the customer: Eliza
Enter the name of the customer: EOF

['Eliza']
['Eliza']
'''


'''
Enter the name of the customer: 1234
Enter the name of the customer: 2345
Enter the name of the customer: 3456
Enter the name of the customer: 4567
Enter the name of the customer: EOF

['1234', '2345', '3456', '4567']
['2345', '3456', '4567', '1234']
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. How did you move the element in the list?

I used "customers.pop(0)" which removes and returns the first item in the list. 
Then using customers.append(first_customer) it will add that first item to the 
end of the list.





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