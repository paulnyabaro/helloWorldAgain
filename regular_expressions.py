import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

# mo is matching objects
a = True
b = False
print(a or a and b and a)

# Regular expressions grouping
phoneNumRegex_two = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo_two = phoneNumRegex_two.search('My number is 415-555-4242.')
print(mo_two.group(1))
print(mo_two.group(2))
print(mo_two.group(0))
print(mo_two.group())
print(mo_two.groups())


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo_three = batRegex.search('Batmobile lost a wheel')
print(mo_three.group())

# ? is used for optional expressions * for zero or more occurrences + is for 1 or more occurrences
# (wo){4} or (wo){2,4} for repeting the pattern the number of times