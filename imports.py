import math
from math import *

print(globals())

float_number = [1.3, 32.3, 432.23, 4234.43, 89.0]

print(sum(float_number))

# Using fsum
print('This is after using fsum function')
print(math.fsum(float_number))


# sum with 0.1 10 times will give 0.99999999999 but with fsum the answer will be 1
numbers = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
print(sum(numbers))
