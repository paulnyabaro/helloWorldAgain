import datetime

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