# FILE NAME - convert_C_to_F_01.py

# NAME: Thomas Caine
# DATE: 09/23/24
# BRIEF DESCRIPTION: This code will have the ability to convert temperature from celsius to fahrenheit 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience



def main():
    convert_C_to_F()



def convert_C_to_F():
    
    # Don't forget to cast user input as a float!
    
    ########## ENTER YER CODE BELOW THIS LINE #########

    temp_question = float(input("Enter temperature in Celsius: "))
    celsius_calculation = ((1.8*temp_question)+32)
    print(f'{temp_question} degrees Celsius is {celsius_calculation} degrees in Fahrenheit')








    ########### END YER CODE ABOVE THIS LINE ###########

main()



########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a temperature in Celsius: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: 1

1 degrees Celsius is 33.8 degrees Fahrenheit.

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does `float` mean?





2. Why do you think it is important to use `float` as opposed to
   a different type of variable type?





'''
