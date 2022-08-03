def get_even_numbers(number=6):
    for num in range(number):
        print((num + 1) * 2)


get_even_numbers(8)


def draw_patters(symbol, num_range):
    for _ in range(num_range):
        print(symbol * _)


draw_patters("*", 8)
draw_patters("-", 18)
draw_patters("^", 16)
draw_patters(num_range=10, symbol='%')

# We can’t provide a positional argument after a keyword argument.


def num_add(num1, num2):
    print(f'Addition of {num1} and {num2} is {num1 + num2}')


def num_sub(num1, num2):
    print(f'{num2} subtracted from {num1} is {num1 - num2}')


def num_div(num1, num2=1):
    try:
        print(f'Division of {num1} to {num2} is {num1 / num2}')
    except ZeroDivisionError:
        print('You can\'t divide by zero')


def num_mul(num1, num2):
    print(f'Multiplication of {num1} and {num2} is {num1 * num2}')


num_add(145, 822)
num_sub(21978, 232)
num_div(32424, 23)
num_mul(98, 3)


def is_palindrome(word):
    word = word.strip().lower()
    reversed_word = reversed(word)

    if list(word) == list(reversed_word):
        print(True)
    else:
        print(False)


is_palindrome("Hannah")
is_palindrome("was it a car or a cat I saw") # This should be a palindrome
