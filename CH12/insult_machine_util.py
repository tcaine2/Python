import random

# You need to add at least five more insults (for a total of at least six)
# Insert your insults into the strings in the list.
insults = [
    'You look like a bunch of rocks',
    'You look like a discount mannequin in a yard sale',
    'You\'re like the leftover spaghetti no one wanted to eat',
    'You have the charm of a wet sock',
    'You\'re the human equivalent of a parking ticket',
    'You look like someone tried to draw a person, but gave up halfway through',
]

def welcome():
    print('---------------------------------')
    print('Welcome to the Insulternator 3500')
    print('---------------------------------')

def show_all_insults():
    print(insults)

def one_insult():
    print(random.choice(insults))

def two_insults():
    one_insult()
    one_insult()
    
def insult_specific_name(name):
    print(f'\n{name}, here is your insult: ', end='')
    one_insult()

def insult_x_number_of_insults(num):
    print()
    for x in range(num):
        one_insult()

def goodbye():
    print()
    print('---------------------------------------------')
    print('Thank you for playing the Insulternator 3500!')
    print('---------------------------------------------')