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