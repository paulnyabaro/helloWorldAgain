# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello world, am {name}, your motherfucking trouble maker.')  # Press Ctrl+F8 to toggle the breakpoint.
    is_tall = True
    guess_answer = "pause"
    guess_word = ""
    guess_counts = 0
    guess_attempts_reached = True
    if is_tall:
        print('And I am tall.🤣🤣🤣🤣')
    while guess_word != guess_answer:
        guess_word = input("What is the guess name")
        guess_counts += guess_counts
    print('You have won')

    squares = [94, 3453, 45, 43, 524, 55, 66, 62, 2]
    for square in squares:
        print(square * square)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Paul')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
