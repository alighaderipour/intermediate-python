# A decorator is a function that takes another function as input
# and extends or modifies its behavior without modifying its code.
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, World!")

say_hello()
