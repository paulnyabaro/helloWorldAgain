import itertools

gym_days = itertools.cycle(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
exercises = itertools.cycle(['Push ups', 'Pull ups', 'Squats', 'Handstand Push ups', 'Dips'])

for days in range(1, 30):
    print(f'Day {days}: ({next(gym_days)}) do {next(exercises)} exercise')
