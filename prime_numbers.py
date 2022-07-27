# # Kienyeji solving for prime numbers
# not_prime_numbers = []
# for numbers in range(100):
#     for divisor in range(2, numbers):
#         if numbers % divisor == 0:
#             not_prime_numbers.append(numbers)
#
# all_numbers = []
# for i in range(2, 100):
#     all_numbers.append(i)
#
# print(set(all_numbers) - set(not_prime_numbers))


dividend = int(input('Please enter a number'))

for divisor in range(2, dividend):
    if dividend % divisor == 0:
        print(f"{dividend} is not prime")
        break
    else:
        print(f"{dividend} is prime")
        break
