import itertools

employees = itertools.cycle(["Peter", "Fiona", "Carl"])
days = itertools.cycle(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

for day_number in range(1, 31):
    print(f"Day {day_number} ({next(days)}): {next(employees)} closes.")
