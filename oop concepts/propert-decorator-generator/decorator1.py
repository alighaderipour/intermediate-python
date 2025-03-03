📌 What Are Decorators in Python?
A decorator in Python is a higher-order function that modifies the behavior of another function or class method without changing its actual code. It allows you to add functionality dynamically.

In simpler terms:

A decorator is a function that takes another function as input.
It wraps the function with additional behavior.
It returns a new function with the modified behavior.
🌱 Understanding Decorators Step-by-Step
1️⃣ Functions Are First-Class Objects
To understand decorators, first, you must know that Python treats functions as first-class objects. This means: ✅ You can assign functions to variables.
✅ You can pass functions as arguments to other functions.
✅ You can return functions from functions.

Example: Functions as First-Class Objects
python
Copy
Edit
def greet(name):
    return f"Hello, {name}!"

# Assigning a function to a variable
hello = greet
print(hello("Alice"))  # Hello, Alice!

# Passing a function as an argument
def shout(func, name):
    return func(name).upper()

print(shout(greet, "Bob"))  # HELLO, BOB!
2️⃣ Functions Inside Functions (Closures)
A decorator is just a function that returns another function. This is known as a closure.

Example: A Function Returning Another Function
python
Copy
Edit
def outer_function():
    def inner_function():
        print("I am inside the outer function!")
    return inner_function  # Returns the inner function

# Assign returned function to a variable
func = outer_function()
func()  # I am inside the outer function!
3️⃣ Simple Decorator (Manually Applying)
A decorator is just a function that takes a function as an argument and returns a new function.

Basic Example: Logging Decorator
python
Copy
Edit
def log_decorator(func):
    def wrapper():
        print(f"Calling function: {func.__name__}")
        func()
        print(f"Finished calling {func.__name__}")
    return wrapper  # Return the modified function

# Define a simple function
def say_hello():
    print("Hello, world!")

# Manually apply the decorator
say_hello = log_decorator(say_hello)

# Call the decorated function
say_hello()
🔹 Output:

bash
Copy
Edit
Calling function: say_hello
Hello, world!
Finished calling say_hello
📝 Using @decorator Syntax
Instead of manually applying the decorator (say_hello = log_decorator(say_hello)), Python provides the @decorator_name syntactic sugar.

Using @ Decorator Syntax
python
Copy
Edit
def log_decorator(func):
    def wrapper():
        print(f"Calling function: {func.__name__}")
        func()
        print(f"Finished calling {func.__name__}")
    return wrapper

@log_decorator  # This applies the decorator
def say_hello():
    print("Hello, world!")

say_hello()
🔹 Output (Same as before):

bash
Copy
Edit
Calling function: say_hello
Hello, world!
Finished calling say_hello
4️⃣ Preserving Function Metadata with functools.wraps
When you apply a decorator, the function name (__name__) and docstring (__doc__) get replaced by the wrapper’s details. To fix this, use functools.wraps.

python
Copy
Edit
import functools

def log_decorator(func):
    @functools.wraps(func)
    def wrapper():
        print(f"Calling function: {func.__name__}")
        func()
        print(f"Finished calling {func.__name__}")
    return wrapper

@log_decorator
def say_hello():
    """This function says hello."""
    print("Hello, world!")

print(say_hello.__name__)  # say_hello (not wrapper)
print(say_hello.__doc__)   # This function says hello.
🚀 Basic, Intermediate, Advanced, and Practical Examples
Let's go step by step.

🔹 3 Basic Examples
1. Timing a Function (Performance Profiler)
python
Copy
Edit
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(2)
    print("Function finished!")

slow_function()
2. Counting Function Calls
python
Copy
Edit
def count_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} called {count} times")
        return func(*args, **kwargs)
    return wrapper

@count_calls
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
3. Converting Function Output to Uppercase
python
Copy
Edit
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase_decorator
def get_message():
    return "hello world"

print(get_message())  # HELLO WORLD
🔹 3 Intermediate Examples
4. Restricting Access Based on User Role
python
Copy
Edit
def require_admin(func):
    def wrapper(user):
        if user.lower() != "admin":
            print("Access denied!")
            return
        return func(user)
    return wrapper

@require_admin
def secret_function(user):
    print(f"Welcome, {user}. You have access!")

secret_function("guest")  # Access denied!
secret_function("admin")  # Welcome, admin. You have access!
5. Retry a Function if It Fails
python
Copy
Edit
import random

def retry_decorator(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            if random.random() < 0.5:  # Simulating failure
                print("Retrying...")
                continue
            return func(*args, **kwargs)
        print("Function failed after 3 retries")
    return wrapper

@retry_decorator
def unstable_function():
    print("Function succeeded!")

unstable_function()
6. Measuring Memory Usage (for Data Science)
python
Copy
Edit
import tracemalloc

def memory_profiler(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"{func.__name__}: Current = {current / 10**6}MB, Peak = {peak / 10**6}MB")
        return result
    return wrapper

@memory_profiler
def create_large_list():
    return [i for i in range(10**6)]

create_large_list()
🎯 4 Practical Examples
API Rate Limiting
Logging API Requests in a Web App
Checking Function Arguments Before Execution
Caching Expensive Computations (Memoization)
I'll write these next—let me know if you want to continue! 🚀







