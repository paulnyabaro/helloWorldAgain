name = input('What is your name? ').strip().title() or 'World'
print(f'Hello {name}')


student_data = {'name': 'Jolie', 'age': 12, 'favorite color': 'pink'}
print(student_data.setdefault('favorite teacher', 'Eveline'))
print(student_data.setdefault('favorite teacher', 'Jane'))
print(student_data.setdefault('age', 10))


message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)
