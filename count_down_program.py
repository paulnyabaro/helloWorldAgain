import time, subprocess

timeLeft = 2
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft -= 1
else:
    subprocess.Popen(['start', 'alarm.wav'],shell=True)
    # print('Time is up')
