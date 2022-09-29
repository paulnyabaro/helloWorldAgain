import asyncio
import time
async def say(delay, msg):
    await asyncio.sleep(delay)
    print(msg)

print("Started at ", time.strftime("%X"))
asyncio.run(say(1,"Good"))
asyncio.run(say(2, "Morning"))
print("Stopped at ", time.strftime("%X"))

# We used the asyncio.sleep function instead of the traditional time.sleep
# function. If the time.sleep function is used, control will not be given back
# to the event loop. That is why it is important to use the compatible asyncio.
