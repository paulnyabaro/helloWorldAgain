import time, subprocess
timeLeft = 60
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft -= 1
else:
    # subprocess.Popen(['start', 'alarm.wav'])
    print('Time is up')