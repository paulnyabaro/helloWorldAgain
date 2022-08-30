name = input('What is your name? ').strip().title() or 'World'
print(f'Hello {name}')


student_data = {'name': 'Jolie', 'age': 12, 'favorite color': 'pink'}
print(student_data.setdefault('favorite teacher', 'Eveline'))
print(student_data.setdefault('favorite teacher', 'Jane'))
print(student_data.setdefault('age', 10))
