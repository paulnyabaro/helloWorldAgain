# Sets are just dictionaries without key value pair
vegetable = {"carrot", "lettuce", "cabbage", "banana", "carrot"}
print(vegetable)

# Defining an empty set
set()

# Adding to a set
# Using add method
vegetable.add("onion")
print(vegetable)

# Using update method
vegetable.update(["potato", "pumpkin"])
print(vegetable)

# Deleting from a set
# Using delete
vegetable.remove("potato")
print(vegetable)

# Using discard -> does not raise an exception if the key is not found
vegetable.discard("cabbage")
print(vegetable)

# Using pop to remove and item
vegetable.pop()
print(vegetable)

# Sets operations
# Union
letters = {"a", "b", "c"}
numbers = {1, 2, 3}

letters_and_numbers = letters.union(numbers)
print(letters_and_numbers)

# Intersection
numbers_divisible_by_two = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24}
numbers_divisible_by_three = {3, 6, 9, 12, 15, 18, 21, 24, 27}
numbers_divisible_by_both_two_and_three = numbers_divisible_by_two.intersection(numbers_divisible_by_three)
print(numbers_divisible_by_both_two_and_three)

# Difference
# Order matters
bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}
print(bundle_1.difference(bundle_2))
print(bundle_2.difference(bundle_1))

# Symmetric difference
# Order does not matter
bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}

print(bundle_1.symmetric_difference(bundle_2))