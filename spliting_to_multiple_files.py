import to_be_imported as ti

print('This is print from this file')

date_of_birth = input('What is your date of birth?')
print(f'You are {ti.calculate_age(date_of_birth)} years old')
