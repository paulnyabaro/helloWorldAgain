
# List comprehensions
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [x + 1 for x in list]
print(list2)

list3 = [x for x in range(20) if x % 2 == 0]
print(list3)