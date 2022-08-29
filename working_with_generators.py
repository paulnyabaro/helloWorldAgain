def first_100_numbers():
    for number in range(1, 101):
        yield number


print(first_100_numbers())
