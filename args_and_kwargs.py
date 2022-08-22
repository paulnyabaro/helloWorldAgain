def mult(*args):
    return args[0] * args[1] * args[2]


print(mult(4, 32, 324))


def add_nums(*args):
    return sum(args)


print(add_nums(1, 23, 43, 342, 432, 2, 12, 42))
