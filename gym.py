import itertools

gym_days = itertools.cycle(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
exercises = itertools.cycle(['Push ups', 'Pull ups', 'Squats', 'Handstand Push ups', 'Dips'])

for days in range(1, 30):
    print(f'Day {days}: ({next(gym_days)}) do {next(exercises)} exercise')


# Converting a list to an iterator
numbers = [1, 2, 3, 4, 5, 6]
numbers_iter = iter(numbers)

print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
