🔹 Understanding Decorators in Python
A decorator in Python is a function that modifies another function 
(or class) without changing its code. It is often used to add functionality dynamically.

At its core, a decorator:

Takes a function as input (higher-order function).
Wraps it inside another function.
Returns the modified function.
🟢 Beginner Examples (Basic Concepts)
1️⃣ Basic Decorator (Understanding Function Wrapping)
python
Copy code
def my_decorator(func):
    def wrapper():
        print("Something before the function runs.")
        func()
        print("Something after the function runs.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
🔹 What Happens?
@my_decorator applies the my_decorator function to say_hello.
The wrapper function runs before and after say_hello(), adding extra behavior.
2️⃣ Decorator with Arguments (Handling Parameters)
python
Copy code
def my_decorator(func):
    def wrapper(name):
        print("Before the function runs.")
        func(name)
        print("After the function runs.")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
🔹 What Happens?
The wrapper(name) function ensures the original greet(name) works properly.
This shows how to pass arguments to a decorated function.
3️⃣ Using functools.wraps (Preserving Function Metadata)
python
Copy code
import functools

def my_decorator(func):
    @functools.wraps(func)  # Preserves original function name & docstring
    def wrapper(*args, **kwargs):
        print("Before function execution.")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    """Adds two numbers."""
    return a + b

print(add(3, 4))  # ✅ Correct output
print(add.__name__)  # ✅ Shows "add" instead of "wrapper"
🔹 Why Use functools.wraps?
Without it, add.__name__ would be "wrapper" instead of "add".
It ensures the decorated function retains its original identity.
🟠 Intermediate Examples (More Practical Use Cases)
4️⃣ Decorator with Arguments (Customizing Decorators)
python
Copy code
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()  # Prints "Hello!" three times
🔹 What Happens?
repeat(n) is a decorator factory that generates decorators dynamically.
5️⃣ Timing Function Execution (Performance Measurement)
python
Copy code
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds.")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Function finished!")

slow_function()
🔹 Why Use This?
Measures execution time of slow_function(), useful for profiling performance.
🔵 Practical Use Cases (Real-World Applications)
6️⃣ Logging Function Calls
python
Copy code
import functools

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def multiply(a, b):
    return a * b

print(multiply(3, 5))
🔹 Why Use This?
Helps debug function calls by logging arguments and results.
7️⃣ Access Control (Checking Permissions)
python
Copy code
def requires_admin(func):
    def wrapper(user_role, *args, **kwargs):
        if user_role != "admin":
            print("Access denied!")
            return
        return func(user_role, *args, **kwargs)
    return wrapper

@requires_admin
def delete_user(user_role, username):
    print(f"User {username} deleted.")

delete_user("admin", "Alice")  # ✅ Works
delete_user("guest", "Bob")   # ❌ Access denied!
🔹 Why Use This?
Restricts function access based on user roles.
🔴 Advanced Use Cases (Deep Concepts)
8️⃣ Class Decorators (Applying Decorators to Classes)
python
Copy code
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Database:
    def __init__(self):
        print("Database instance created!")

db1 = Database()
db2 = Database()
print(db1 is db2)  # ✅ True, only one instance exists
🔹 Why Use This?
Ensures only one instance of Database is created (Singleton Pattern).
9️⃣ Applying Multiple Decorators (Stacking Decorators)
python
Copy code
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds.")
        return result
    return wrapper

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@timer
@log_calls
def compute(a, b):
    time.sleep(1)
    return a + b

print(compute(2, 3))
🔹 How Stacking Works?
@log_calls wraps compute(), then @timer wraps the result.
The execution order is inside-out, meaning:
log_calls runs first.
Then timer measures execution time.
📌 Summary
Level   Example Concept
🟢 Beginner  Simple Function Wrapping    Basic structure of a decorator
🟢 Beginner  Handling Arguments  Passing values to decorated functions
🟢 Beginner  functools.wraps Preserving function metadata
🟠 Intermediate  Decorator with Arguments    Dynamic decorators
🟠 Intermediate  Timing Execution    Performance measurement
🔵 Practical Logging Calls   Debugging function calls
🔵 Practical Access Control  Restricting function execution
🔴 Advanced  Class Decorator (@singleton)    Controlling object creation
🔴 Advanced  Stacking Decorators Combining multiple decorators
🔹 Final Thoughts
Decorators modify function behavior without changing its code.
They are useful for logging, security, caching, timing, and access control.
Understanding functools.wraps and *args, **kwargs is key.
Start with simple examples and build up gradually.
Would you like me to go deeper into any specific part? 🚀






