
# List comprehensions
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [x + 1 for x in list]
print(list2)

list3 = [x for x in range(20) if x % 2 == 0]
print(list3)

# Dictionary comprehensions
dict = {'a': 21, 'b': 23, 'c': 42, 'd': 68, 'e': 123, 'f': 153}
dict2 = {x:int(y/2) for (x, y) in dict.items() if y <=200}
print(dict2)

# Set comprehensions
list1 = [1, 2, 6, 4, 5, 6, 7, 8, 9, 10, 8]
set1 = {x for x in list1 if x % 2 == 0}
print(set1)