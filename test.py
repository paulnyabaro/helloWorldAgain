for i in range(19):
    print(i ** 3)

randon_array = ['marry', 'had', 'a', 'little', 'lamb']
for arr in randon_array:
    print(arr)

for i in range(15):
    if i > 0:
        print(str(i) + ' -' + i * '*-')

for i in range(-23, 34):
    print(i)

prime_numbers = 0
for n in range(2, 20):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
        prime_numbers += 1

print('The total prime numbers between 0 and ' + str(n + 1) + ' is ' + str(prime_numbers))

a, b = 0, 1
while a < 1000000000:
    print(a)
    a, b = b, a + b


def convert_minutes_to_hours(n):
    days = n // (60 * 24)
    rem_days = n % (60 * 24)
    hours = rem_days // 60
    rem_minutes = rem_days % 60
    print(f'{n} minutes to days, hours and minutes is {days} days {hours} hours and {rem_minutes} minutes')


convert_minutes_to_hours(58779)


y = [2, 12, 3]
z = sorted(y)
print(z)

