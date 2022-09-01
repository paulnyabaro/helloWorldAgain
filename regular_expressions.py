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
# (wo){4} or (wo){2,4} or (wo){4,} or (wo){,4} for repeting the pattern the number of times
# Using search and findall method
# ^ begins with


# SUMMARY
"""The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a non-greedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character,
respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the brackets."""

# sub() is used to substitute string in re
# ignore spaces in order to write an easy-to-read expression
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
# can be written like with triple quote
phoneTwoRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
\d{3}
(\s|-|\.)
\d{4}
(\s*(ext|x|ext.)\s*\d{2,5})?
)''', re.VERBOSE)
