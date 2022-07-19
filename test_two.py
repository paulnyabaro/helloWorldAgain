print("python" > "pythoN")
print([1, 2, 3] == [3, 2, 1])
print(7 == 7.0)
a = [1, 2, 3]
print(id(a))

b = a
print(a is b)  # True

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
print(new_numbers)

numbers_two = [1, 2, 3, 4]
numbers_two.append(5)

print(new_numbers == numbers_two)
