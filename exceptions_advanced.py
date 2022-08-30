numbers = [1, 2, 3, 4, 5]

try:
    print(numbers[100])  # <- Out of range index
except LookupError as ex:
    print(f"Error: {ex}")
    print(type(ex))

# Raising exceptions
# we can use the keyword raise
raise TimeoutError('This is just an exception for no reason')


# The message put in the parenthesis will be shown once the exception is shown
