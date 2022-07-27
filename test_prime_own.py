prime_numbers = []
not_prime_numbers = []
for numbers in range(100):
    for divisor in range(2, numbers):
        if numbers % divisor == 0:
            not_prime_numbers.append(numbers)
            break
        else:
            prime_numbers.append(numbers)
            break

print(f"The prime numbers are: {prime_numbers}")
print(f"The non prime numbers are: {not_prime_numbers}")


