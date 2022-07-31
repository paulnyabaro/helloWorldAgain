import math
import time
from tqdm import tqdm

result = []

for i in tqdm(range(1400)):
    result.append(math.factorial(i))


# Or use the list comprehension
result = [math.factorial(x) for x in tqdm(range(8000))]
