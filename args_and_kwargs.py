def mult(*args):
    return args[0] * args[1] * args[2]


print(mult(4, 32, 324))


def add_nums(*args):
    return sum(args)


print(add_nums(1, 23, 43, 342, 432, 2, 12, 42))

# You can use a descriptive argument name in the function


def display_names(*names):
    print('The names in the Family Guy show are:')
    for name in names:
        print(name)


display_names('Bryan', 'Peter', 'Griffins', 'Stewie', 'Loes', 'Meg')

# Creating dictionary using the dict keyword
person = dict(name="Phil", age=29, city="Budapest", nationality="British")
print(person)

