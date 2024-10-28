# FILE NAME - file_reader.py

# NAME: Thomas Caine
# DATE: 10/28/24
# BRIEF DESCRIPTION:  This lab is intended to explore file reading capabilities with Python. In this lab, 
# there are three different files on the server - words01.txt, words02.txt, and words03.txt. The lab will 
# ask the user for the name of a file and then output the contents.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience




def main():
    file_reader()

def file_reader():
    '''
    This function will ask the user to input a file name. The
    file will be opened and the contents will be output
    to the screen.
    '''
    user = input('File name? ')

    if(user == 'words01.txt'):
        file = open('words01.txt', 'r')
        for line in file:
            print(line, end="")

    elif(user == 'words02.txt'):
        file = open('words02.txt', 'r')
        for line in file:
            print(line, end="")

    elif(user == 'words03.txt'):
        file = open('words03.txt', 'r')
        for line in file:
            print(line, end="")

main()

########################################
#          SAMPLE OUTPUT
########################################

'''
File name? words01.txt

Wolverine
Rogue
Psylocke
Professor X
Beast
'''


'''
File name? words02.txt

Lily
Marshall
Barney
Robin
Ted
'''


'''
File name? words03.txt

blubber
macadamia
gazebo
spatula
plethora
ploy
foible
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is an example of a time when you might want to output the contents
   of a file?

In a setting where the user needed to edit or review files, you could read a file and output its contents based on what you needed the user to do






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