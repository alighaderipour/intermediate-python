import os
os.system('cls' if os.name == 'nt' else 'clear')

def log_decorator(func):
    def wrapper():
        print(f"Calling function: {func.__name__}")
        func()
        print(f"Finished calling {func.__name__}")
    return wrapper

@log_decorator
def say_hello():
    """this function says hello."""
    print("Hello, world!")

print(say_hello.__name__)  # say_hello (not wrapper)
print(say_hello.__doc__)   # This function says hello.