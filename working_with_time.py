import time

print(time.time())

#The result is how many seconds have passed between the Unix epoch and the moment time.time() was called

# Getting time difference
def calcProd():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product
startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))

# Working with sleep
for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)

time.sleep(5) # Next prompt wont appear until this time has passed
# ctrl -C will not interrupt time.sleep() calls

# except KeyboardInterrupt:
# We handle this to prevent the program from crashing