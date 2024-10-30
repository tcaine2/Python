def main():
    fortune_machine

def fortune_machine():
    
    import random
    
    fortunes = []
    user_fortune = None

    while user_fortune != 'DONE':
        user_fortune = input('Enter a fortune: ')
        fortunes.append(user_fortune)
    
    user_fortune.pop()

    # print(random.chooice(fortunes))
    # yes_no = input('Another fortune (y/n)? )

    yes_no = 'y'

    while yes_no == 'y':
        print(random.choice(fortunes))
        yes_no = input('Another fortune (y/n)? ')

main()