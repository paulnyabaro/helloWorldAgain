from typing import Callable

def example_decorator(func: Callable) -> Callable:
    def inner():
        print(f"Now calling {func.__name__}...")
        func()
        print(f"{func.__name__} has ended.")

    return inner

def example_decorator_2(func: Callable) -> Callable:
    def inner_2():
        print(f"Now calling {func.__name__}...")
        func()
        print(f"{func.__name__} has ended.")

    return inner_2

def greeter():
    print("Hello!")

greeter = example_decorator(greeter)
greeter()