import random

heads = 0
tails = 0
for i in range(0, 1000):
    if random.randint(0 ,1):
        heads += 1
    else:
        tails += 1

    if i == 499:
        print(f'Halfway results Heads: {heads} Tails: {tails}')

print(f'Full-time results: {heads} and Tails: {tails}')