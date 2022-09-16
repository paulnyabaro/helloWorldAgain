import datetime
import time

print(datetime.datetime.now())
dt = datetime.datetime(2022, 9, 16, 5, 28, 39)
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)


print(f'Time passed since I created this code: {datetime.datetime.now() - dt}')

# converting from timestamp
print(datetime.datetime.fromtimestamp(1000000000))
print(datetime.datetime.fromtimestamp(time.time()))

# Timedelta --> Represents a duration rather than moment in time
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())

# The datetime.timedelta() function takes keyword arguments weeks, days, hours,
# minutes, seconds, milliseconds, and microseconds.

# There is no month or year key-word argument because “a month” or “a year” is a variable amount of time
# depending on the particular month or year.

# Get the date of the day 1000 days from now
dt = datetime.datetime.now()
thousand_days = datetime.timedelta(days=1000)
print(dt + thousand_days)