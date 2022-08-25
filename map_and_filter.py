def square(num):
    return num ** 2


numbers = [1, 3, 4, 6, 3, 9]
squared_numbers = map(square, numbers)
#
# for number in squared_numbers:
#     print(number)

# Using * to upack the iterables
print(*squared_numbers, sep=', ')


# Using the filter function
numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = filter(lambda number: number % 2 == 0, numbers)
print(*even_numbers, sep=', ')


# Using None with filter
values = [0, "Hello", [], {}, 435, -4.2, ""]
truthy_values = filter(None, values)

print(*truthy_values, sep=", ")