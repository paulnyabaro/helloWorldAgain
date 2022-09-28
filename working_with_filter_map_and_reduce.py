from functools import reduce

# Map
def square(num):
    return num * num
mylist = [1, 2, 3, 4, 5]
new_list = list(map(square, mylist))
print(new_list)

def product(num1, num2):
    return num1 * num2
mylist1 = [1, 2, 3, 4, 5]
mylist2 = [6, 7, 8, 9]
new_list = list(map(product, mylist1, mylist2))
print(new_list)


# Filter
def is_even(num):
    return (num % 2 == 0)
mylist = [1, 2, 3, 4, 5,6,7,8,9]
new_list = list(filter(is_even, mylist))
print(new_list)

# Filter
def seq_sum(num1, num2):
    return num1+num2
mylist = [1, 2, 3, 4, 5]
result = reduce(seq_sum, mylist)
print(result)

# Using Lambda with map
# mylist = [1, 2, 3, 4, 5]
# new_list = list(map(lambda x: x*x, mylist))
# print(new_list)