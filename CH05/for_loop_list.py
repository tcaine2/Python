# FILE NAME - for_loop_list.py

# NAME: Thomas Caine
# DATE: 10/21/24
# BRIEF DESCRIPTION: This lab will merely print out every item in a list using a for loop. 
# The code to grab the dog names from the user is already completed.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



def main():
    doggo_names = get_doggo_names()
    output_names(doggo_names)

def get_doggo_names():
    name = ''
    names = []
    while name != 'DONE':
        name = input('Name of doggo: ')
        if name != 'DONE':
            names.append(name)
    
    return names

def output_names(doggo_names):

    ########## ENTER YER CODE BELOW THIS LINE ##########
    
    print()
    for name in doggo_names:
        print(f'{name} is awesome.')
    
    ########### END YER CODE ABOVE THIS LINE ###########
main()


########################################
#          SAMPLE OUTPUT
########################################

'''
Name of doggo: Maggie
Name of doggo: Quinnie
Name of doggo: Yogi
Name of doggo: BB-8
Name of doggo: DONE

Maggie is awesome.
Quinnie is awesome.
Yogi is awesome.
BB-8 is awesome.
'''


'''
Name of doggo: a
Name of doggo: b
Name of doggo: c
Name of doggo: DONE

a is awesome.
b is awesome.
c is awesome.
'''


'''
Name of doggo: DONE
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
[ X ] I pretty much get it.
[ ] I'm solid. Totally got it.

'''