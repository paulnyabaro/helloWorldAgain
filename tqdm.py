import math
import time
from tqdm import tqdm

result = []

for i in tqdm(range(1400)):
    result.append(math.factorial(i))
