import random

heads = 0
tails = 0
for i in range(0, 1001):
    if random.randint(0 ,1):
        heads += 1
    else:
        tails += 1

print(f'Heads came {heads} while tails came {tails}')