import time, subprocess

timeLeft = 2
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft -= 1
else:
    file = subprocess.Popen(['xdg-open', 'alarm.wav'])
    # print('Time is up')
    file.wait(1)
    file.kill()
