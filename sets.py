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
