from functools import wraps
from time import perf_counter
from typing import Callable, List, Set

def stopwatch(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = perf_counter()
        func(*args, **kwargs)
        stop_time = perf_counter()

        print(f"{func.__name__} ran in {stop_time - start_time:.5f}s")

    return inner

@stopwatch
def make_list(size: int) -> List:
    return list(range(size))

@stopwatch
def make_set(size: int) -> Set:
    return set(range(size))

make_list(100_000)  # make_list ran in 0.00407s
make_set(100_000)   # make_set ran in 0.00628s