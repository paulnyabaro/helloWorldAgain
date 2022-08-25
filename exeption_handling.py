while True:
    try:
        number = int(input('Enter a number'))
        break
    except ValueError:
        print('You did not enter a valid number, please try again!')

    except TypeError:
        print('The entered value is not a digit')


# Multiple excepts in the same statement
# except(ValueError, TypeError)

# Using else in the exception statement

while True:
    try:
        print(20 / 0)
    except ZeroDivisionError:
        print('You can\'t divide by zero')
    else:
        print('Done')
    finally:
        print('Must print no matter what happens')


