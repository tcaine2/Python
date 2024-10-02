# FILE NAME - triangle_area.py

# NAME: Thomas Caine
# DATE: 9/18/24
# BRIEF DESCRIPTION:  This is a program that uses the height and the base of a triangle to 
# compute the area of the triangle using the formula A = 1/2 * b * h.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience



def main():
    find_area()



def find_area():

    ########## ENTER YER CODE BELOW THIS LINE ##########
    
    triangle_height = float(input("Enter the height: "))
    triangle_base = float(input("Enter the base: "))
    area_calculation = 0.5*triangle_base*triangle_height
    print(f'The area of the triangle is {area_calculation}')

    ########### END YER CODE ABOVE THIS LINE ###########

main()



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter the height: 1
Enter the base: 1

The area of the triangle is 0.5

'''



'''

Enter the height: 8
Enter the base: 4

The area of the triangle is 16.0

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is the flow of the program? Which line of code kicks off the process?

I had the flow of this program defining what you should set the base and height to and then putting them into the area of a triangle formula to output everything together
The line that "kicks off" the program would be setting the triangle height



2. What was the hardest part of this lab?

For me it was figuring out how to put everything together to calculate. 



'''
