import to_be_imported as ti

print('This is print from this file')

date_of_birth = input('What is your date of birth? ')
print(f'You are {ti.calculate_age(date_of_birth)} years old')


# Testing random code from twitter
align = '<'
fill_char = '*'
width = 25
s = 'Python'
print(f'{s:{fill_char}{align}{width}}')

