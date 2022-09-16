import time

for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)

time.sleep(5) # Next prompt wont appear until this time has passed
# ctrl -C will not interrupt time.sleep() calls