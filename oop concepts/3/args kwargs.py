In Python, *args and **kwargs allow us to handle a variable number of arguments in functions flexibly.

*args allows a function to accept any number of positional arguments as a tuple.
**kwargs allows a function to accept any number of keyword arguments as a dictionary.
🔹 Beginner Examples (Covering the Basics)
Example 1: Using *args to Accept Multiple Arguments
*args collects all positional arguments into a tuple.

python
Copy
Edit
def add_numbers(*args):
    print(args)  # Just to show what `args` contains
    return sum(args)

print(add_numbers(1, 2, 3, 4))  # Output: (1, 2, 3, 4) then 10
print(add_numbers(5, 10))       # Output: (5, 10) then 15
✅ Key Concept: *args allows passing multiple arguments without explicitly defining them.

Example 2: Using **kwargs to Accept Keyword Arguments
**kwargs collects all keyword arguments into a dictionary.

python
Copy
Edit
def print_user_details(**kwargs):
    print(kwargs)  # Just to show what `kwargs` contains
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_details(name="Alice", age=30, city="New York")
Output:

pgsql
Copy
Edit
{'name': 'Alice', 'age': 30, 'city': 'New York'}
name: Alice
age: 30
city: New York
✅ Key Concept: **kwargs allows passing multiple named arguments without explicitly defining them.

Example 3: Mixing *args and **kwargs
You can use both *args and **kwargs in the same function.

python
Copy
Edit
def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

display_info(1, 2, 3, name="Alice", age=30)
Output:

matlab
Copy
Edit
Positional arguments: (1, 2, 3)
Keyword arguments: {'name': 'Alice', 'age': 30}
✅ Key Concept: *args captures unnamed values, while **kwargs captures named values.

🔹 Intermediate Examples
Example 4: Unpacking Arguments from Lists/Tuples
You can use * to unpack a list or tuple into a function.

python
Copy
Edit
def multiply(x, y, z):
    return x * y * z

nums = (2, 3, 4)
result = multiply(*nums)  # Unpacking the tuple into the function
print(result)  # Output: 24
✅ Key Concept: * unpacks values from a tuple or list.

Example 5: Unpacking Arguments from Dictionaries
You can use ** to unpack a dictionary into keyword arguments.

python
Copy
Edit
def greet(name, age, city):
    print(f"Hello, my name is {name}, I am {age} years old and I live in {city}.")

person_info = {"name": "Alice", "age": 30, "city": "New York"}
greet(**person_info)  # Unpacking the dictionary into function parameters
Output:

pgsql
Copy
Edit
Hello, my name is Alice, I am 30 years old and I live in New York.
✅ Key Concept: ** unpacks a dictionary into keyword arguments.

🔹 Practical Use Cases of *args and **kwargs in Decorators
Example 6: Logging Decorator Using *args and **kwargs
A decorator that logs function calls and arguments.

python
Copy
Edit
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(3, 5))
✅ Key Concept: The decorator works for any function, thanks to *args and **kwargs.

Example 7: Timing Decorator
Measure execution time of a function.

python
Copy
Edit
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function(n):
    time.sleep(n)

slow_function(2)
✅ Key Concept: *args and **kwargs allow the decorator to work on any function.

🔹 Advanced Decorator Use Cases
Example 8: A Decorator That Modifies Function Behavior Based on Arguments
A decorator that repeats a function call n times.

python
Copy
Edit
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)  # Calls function 3 times
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
✅ Key Concept: repeat(n) uses *args and **kwargs to call the function multiple times.

Example 9: A Class-Based Decorator That Tracks Function Calls
A decorator that keeps count of how many times a function is called.

python
Copy
Edit
class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)

@CallCounter
def say_hello():
    print("Hello!")

say_hello()
say_hello()
say_hello()
✅ Key Concept: *args and **kwargs allow tracking function calls dynamically.

🔥 Summary
Beginner

*args for multiple positional arguments
**kwargs for multiple keyword arguments
Combining *args and **kwargs
Intermediate

Unpacking arguments from lists/tuples (*args)
Unpacking arguments from dictionaries (**kwargs)
Practical Decorators

Logging function calls
Measuring execution time
Advanced Decorators

A decorator with arguments (repeat(n))
A class-based decorator (CallCounter)
