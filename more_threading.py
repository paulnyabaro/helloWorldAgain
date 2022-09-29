from threading import current_thread, Thread as Thread
from time import sleep

def print_hello():
    sleep(2)
    print("{}: Hello".format(current_thread().name))

def print_message(msg):
    sleep(1)
    print("{}: {}\n".format(current_thread().name, msg))

# create threads
t1 = Thread(target=print_hello, name="Th 1")
t2 = Thread(target=print_hello, name="Th 2")
t3 = Thread(target=print_message, args=["Good morning"], name="Th 3")

# start the threads
t1.start()
t2.start()
t3.start()

# wait till all are done
t1.join()
t2.join()
t3.join()