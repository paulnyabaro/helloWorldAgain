import random

my_guess_number = random.randint(1, 20)
try:
    user_guess_number = int(input('Guess a number between 1 and 20 '))
except ValueError:
    print('Only number are allowed here')
    user_guess_number = int(input('Guess a number between 1 and 20 '))
guess_times = 0

while my_guess_number != user_guess_number:
    if user_guess_number > 20 or user_guess_number < 1:
        print('Your number is outside the range. Try again ')
        user_guess_number = int(input())
        guess_times += 1
    elif user_guess_number > my_guess_number:
        print('Your guess is too high! Try again ')
        user_guess_number = int(input())
        guess_times += 1
    else:
        print('Your guess is too low! Try again ')
        user_guess_number = int(input())
        guess_times += 1
else:
    print(f'Good job. After {guess_times} guess(es), you got it right, my number was {my_guess_number}')
