from random import randint

options = ['rock', 'paper', 'scissors']
value = randint(0, 2)
comp_option = options[value]
print('The computer chose ' + options[value])

user_option = input('''
Choose an option
r: rock
p: paper
s: Scissors
q: quite
\n
''')

while user_option == 'r' or user_option == 'p' or user_option == 's' or user_option == 'q':
    if user_option == 'r':
        if comp_option == options[0]:
            print('Your draw')
        elif comp_option == options[1]:
            print('You lost')
        else:
            print('You won')
        break

    elif user_option == 'p':
        if comp_option == options[0]:
            print('Your won')
        elif comp_option == options[1]:
            print('You draw')
        else:
            print('You lost')
        break

    elif user_option == 's':
        if comp_option == options[0]:
            print('Your lose')
        elif comp_option == options[1]:
            print('You wom')
        else:
            print('You draw')
        break

    else:
        exit()
else:
    user_option = input('''Invalid option try again!''')

