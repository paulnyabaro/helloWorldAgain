def first_100_numbers():
    for number in range(1, 101):
        yield number


print(first_100_numbers())

g = first_100_numbers()
# The result is an iterator
print(next(g))
print(next(g))
print(next(g))
