import threading, time

print('Start of the program')


def take_a_nap():
    time.sleep(5)
    print('Wake up!')


thread_obj = threading.Thread(target=take_a_nap)
thread_obj.start()
print('End of the program')

# Starting other programs
# Popen() function in the built-in subprocess module starts other programs (p -> process, then open)
import subprocess
subprocess.Popen('/usr/bin/gnome-calculator')
calc = subprocess.Popen('/usr/bin/gnome-calculator')
print(calc.poll())
print(calc.wait())

# Opening a file with the respective application
# subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\hello.txt'])