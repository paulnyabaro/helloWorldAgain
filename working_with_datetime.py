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

# Timedelta
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
delta.total_seconds()
