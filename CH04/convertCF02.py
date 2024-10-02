# FILE NAME - convertCF02.py

# NAME: Thomas Caine
# DATE: 10/2/24
# BRIEF DESCRIPTION: This lab will ask the if they would like to convert from Celsius to Fahrenheit or from Fahrenheit to Celsius and then output
# based on what the input



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience




def main():
    convertCF2()

def display_menu():
    print('===== Temperature Converter =====')
    print()
    print('  1. Convert from Celsius to Fahrenheit')
    print('  2. Convert from Fahrenheit to Celsius')
    print()

def convertCF2():
    display_menu()

    ########## ENTER YER CODE BELOW THIS LINE ##########

    temperature = input('Enter a temperature to input ')
    
    convert_option_1 = 1
    option_1 = temperature * 9/5 + 32

    convert_option_2 = 2
    option_2 = (temperature - 32 ) * 5/9

    menu_options = input('Please choose from the above menu: ')

    print(menu_options)
    print(temperature)

    if temperature == option_1:
      print(f'{temperature}degrees Celsius is{option_2}degrees Fahrenheit')
    else:
      print(f'{temperature}degrees Fahrenheit is{option_1}degrees Celsius')








    ########### END YER CODE ABOVE THIS LINE ###########





main()



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?







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
