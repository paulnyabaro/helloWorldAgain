# This is a list though
names = ['kev', 'jan', 'line', 'ken', 'juanpa', 'zurita']
print(names)
names.sort()
print(names)


# Dictionaries here
student = {'name': 'John Smith', 'D.o.B': '1999'}

student_two = {
    'name': 'James Wayne',
    'subjects': ['English', 'Mathematics', 'Science'],
    'graders': [79, 88, 92]
}

student_three = {
    ('James', 'Web', 'Telescope'): 'This is the name',
    1: 'This is the position'
}


print(student['name'])
print(student_three[('James', 'Web', 'Telescope')])
print(student_three[1])

# Using the get and parenthesis --- returns None if key not found you can also define a default value
print(student.get('name'))
print(student.get('names', 'Not found'))

# Adding to a dictionary
student['gender'] = 'Male'
print(student)

# Adding to a dictionary using the update method
movie = {
    'name': 'The avengers end game',
    'budget': 2_000_000
}

movie_meta = {
    'Director': 'Jim Thompson Lie',
    'Profit': 389_000_000
}

movie.update(movie_meta)

print(movie)