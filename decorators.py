from typing import Callable

def example_decorator(func: Callable) -> Callable:
    def inner():
        print(f"Now calling {func.__name__}...")
        func()
        print(f"{func.__name__} has ended.")

    return inner