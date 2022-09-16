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


# Using sleep to pause a program until a certain time is reached
import datetime
import time
halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2016:
    time.sleep(1)
else:
    print('Not time to sleep')


# strftime directiveMeaning
# %YYear with century, as in '2014'
# %yYear without century, '00' to '99' (1970 to 2069)
# %mMonth as a decimal number, '01' to '12'
# %BFull month name, as in 'November'
# %bAbbreviated month name, as in 'Nov'
# %dDay of the month, '01' to '31'
# %jDay of the year, '001' to '366'
# %wDay of the week, '0' (Sunday) to '6' (Saturday)
# %AFull weekday name, as in 'Monday'
# %aAbbreviated weekday name, as in 'Mon'
# %HHour (24-hour clock), '00' to '23'
# %IHour (12-hour clock), '01' to '12'
# %MMinute, '00' to '59'
# %SSecond, '00' to '59'
# %p'AM' or 'PM'
# %%Literal '%' character