import itertools

gym_days = itertools.cycle(['Monday', 'Wednesday', 'friday'])
exercises = itertools.cycle(['Push ups', 'Pull ups', 'Squats', 'Handstand Push ups', 'Dips', 'Traditional sit ups'])

for days in range(1, 30):
    print(f'For day {days}: {next(gym_days)} do {next(exercises)} exercise')
