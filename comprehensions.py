names = ['James', 'Lilian', 'Kelly', 'EVERLYNE', 'pAULinE']
processed_names = []

# The traditional way
for name in names:
    processed_names.append(name.title())

print(processed_names)

# Using comprehension
processed_names_2 = [name.title() for name in names]
print(processed_names_2)

# Replacing the old list with the new one
names = [name.title() for name in names]
print(names)

# A more complex example
names = ['Kay', 'Jane', 'priscilla', 'cecile', 'keiTh']
ages = [32, 32, 42, 26, 21]

person_data = []

for name, age in zip(names, ages):
    person_info = name, age
    person_data.append(person_info)

print(person_data)

# A more sophisticated approach
people_data = [(name.title(), age) for name, age in zip(names, ages)]
print(people_data)

# Set comprehensions
names = ['Kay', 'Jane', 'priscilla', 'cecile', 'keiTh', 'keith', 'KEITH']
names = {name for name in names}
print(names)
names = {name.title() for name in names}
print(names)

# Dictionaries comprehensions
names = ['Kay', 'Jane', 'priscilla', 'cecile', 'keiTh']
ages = [32, 32, 42, 26, 21]

student_data = {
    student_name: student_age
    for student_name, student_age in
    zip(names, ages)
}
print(student_data)