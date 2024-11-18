# FILE NAME - fortune_machine.py

# NAME: Thomas Caine
# DATE: 11/18/24
# BRIEF DESCRIPTION: This lab will explore importing custom modules. In this case, 
# the code will use the fortune_util module that was provided and it will be used 
# to craft a program that provides a good experience for the user. 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience




import fortune_util

def main():
    run_fortune_machine()

def run_fortune_machine():

    ########## ENTER YER CODE BELOW THIS LINE ##########

    fortune_util.get_directions()
    fortune_util.dashes()
    print('ONE FORTUNE:')
    fortune_util.get_one_fortune()
    fortune_util.dashes()
    print('MULTIPLE FORTUNES:')
    number_of_fortunes = int(input(f'How many fortunes would you like? '))
    fortune_util.get_multiple_fortunes(number_of_fortunes)
    fortune_util.dashes()
    fortune_util.quit()

    ########### END YER CODE ABOVE THIS LINE ###########


main()



########################################
#          SAMPLE OUTPUT
########################################

'''

--------------------------------------------------
Welcome to the Fortune Telling Machine

The instructions are simple - you may request one
fortune, you  may request multiple fortunes, or you
may request to quit.

Please enjoy your fortune(s)! But beware! When you use
the Fortune Telling Machine, you get what you get and
you don't get upset!

--------------------------------------------------
ONE FORTUNE:
There's a lot of atoms in you.


--------------------------------------------------
MULTIPLE FORTUNES:
How many fortunes would you like? 7

1 - Bring an umbrella today.

2 - There's a lot of atoms in you.

3 - You will live a long, prosperous life.

4 - Chin up! It's going to be a great day!

5 - If you have no pockets, your phone can't fall out of them!

6 - Chin up! It's going to be a great day!

7 - You will live a long, prosperous life.

--------------------------------------------------

I hope you enjoyed your fortunes...

'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 

I had to determine how we could reference the code written in the utility file and by doing that we would write fortune_util.get_directions()




2. What value do you see in having external modules?

This makes for a much easier final code to understand if someone was to look at this. They could easily go back to the utility file and determine what
each defined varible is that is being called over to the final code.




'''


