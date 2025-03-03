Great! Let’s dive into real-world practical uses of decorators that professional Python developers use in production code. These examples cover scenarios in web development, data science, performance optimization, security, and more.

🔥 1. API Rate Limiting (Throttling Requests)
In web applications, you often need to limit the number of requests a user can make within a time frame.

Example: Limiting Function Calls Per Minute
python
Copy
Edit
import time
from functools import wraps

def rate_limit(max_calls, time_period):
    calls = []

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            # Remove outdated calls
            while calls and calls[0] < now - time_period:
                calls.pop(0)

            if len(calls) < max_calls:
                calls.append(now)
                return func(*args, **kwargs)
            else:
                print("Too many requests! Try again later.")
        return wrapper
    return decorator

@rate_limit(max_calls=3, time_period=5)  # Max 3 calls per 5 seconds
def fetch_data():
    print("Fetching data...")

# Simulating multiple API calls
fetch_data()
fetch_data()
fetch_data()
fetch_data()  # Too many requests!
🔹 Where is this used?

API Rate Limiting (e.g., Django REST Framework)
Preventing abuse in APIs (e.g., login attempts)
🔍 2. Logging API Requests in Web Apps
Professional developers use decorators to log function calls in Flask, FastAPI, and Django applications.

Example: Logging API Calls
python
Copy
Edit
import functools
import datetime

def log_requests(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with open("requests.log", "a") as f:
            f.write(f"{datetime.datetime.now()} - Called {func.__name__} with {args}, {kwargs}\n")
        return func(*args, **kwargs)
    return wrapper

@log_requests
def process_payment(user, amount):
    print(f"Processing payment of ${amount} for {user}.")

process_payment("Alice", 100)
🔹 Where is this used?

Web APIs (Flask, FastAPI)
Debugging API requests
🔐 3. User Authentication & Authorization
You often need to restrict access to certain functions in web applications.

Example: Checking If User Is Logged In
python
Copy
Edit
def require_login(func):
    def wrapper(user, *args, **kwargs):
        if user.get("logged_in"):
            return func(user, *args, **kwargs)
        else:
            print("Access denied! Please log in.")
    return wrapper

@require_login
def view_dashboard(user):
    print(f"Welcome, {user['name']}! Here is your dashboard.")

# Simulating users
user1 = {"name": "Alice", "logged_in": True}
user2 = {"name": "Bob", "logged_in": False}

view_dashboard(user1)  # ✅ Allowed
view_dashboard(user2)  # ❌ Access Denied
🔹 Where is this used?

Web frameworks (Django, Flask, FastAPI)
Role-based access control (RBAC)
⚡ 4. Caching Expensive Computations
When working with machine learning, databases, or API calls, caching results improves performance.

Example: Memoization (Cache Results of Expensive Functions)
python
Copy
Edit
import functools

def memoize(func):
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print("Fetching from cache:", args)
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Faster due to caching!
print(fibonacci(10))  # Fetching from cache
🔹 Where is this used?

Avoiding repeated expensive function calls
Machine learning computations
Web API responses
💡 5. Validating Function Arguments
A decorator can check function arguments before execution, preventing errors.

Example: Checking If Inputs Are Positive Numbers
python
Copy
Edit
def validate_positive(func):
    def wrapper(*args, **kwargs):
        if any(arg < 0 for arg in args):
            raise ValueError("Arguments must be positive!")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_area(length, width):
    return length * width

print(calculate_area(5, 10))  # ✅ Works
# print(calculate_area(-5, 10))  # ❌ Raises ValueError
🔹 Where is this used?

Data validation in APIs
Preventing incorrect user inputs
📊 6. Measuring Execution Time (Profiling Code)
Used by data scientists & performance engineers to analyze code efficiency.

Example: Timing a Function
python
Copy
Edit
import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Done!")

slow_function()
🔹 Where is this used?

Performance testing
Detecting slow functions in big data processing
🔄 7. Retrying a Function on Failure
In network programming (e.g., APIs, databases), failures can happen. You need to retry automatically.

Example: Retrying API Calls
python
Copy
Edit
import time
import random

def retry(max_retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                if random.random() > 0.3:  # Simulating success 70% of the time
                    return func(*args, **kwargs)
                print(f"Attempt {attempt+1} failed. Retrying...")
                time.sleep(1)
            print("Function failed after maximum retries.")
        return wrapper
    return decorator

@retry(max_retries=5)
def fetch_data():
    print("Fetching data... Success!")

fetch_data()
🔹 Where is this used?

Handling unstable APIs
Database connections
Retrying failed network requests
🎯 8. Sending Alerts When Function Fails
Professional applications send emails or logs when critical functions fail.

Example: Logging Errors to a File
python
Copy
Edit
import functools
import traceback

def log_errors(filename="errors.log"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                with open(filename, "a") as f:
                    f.write(f"Error in {func.__name__}: {str(e)}\n")
                    f.write(traceback.format_exc() + "\n")
                print("An error occurred. Check logs for details.")
        return wrapper
    return decorator

@log_errors()
def risky_function():
    return 1 / 0  # This will cause an error

risky_function()
🔹 Where is this used?

Logging errors in production systems
Debugging failed jobs in machine learning pipelines
🎯 Summary: Where Do Pro Programmers Use Decorators?
✅ Web Applications: Authentication, API logging, rate limiting
✅ Data Science & ML: Caching, profiling, memory optimization
✅ Security: Input validation, permission checks
✅ Performance Optimization: Retrying failed operations, measuring speed

These are real-world decorator use cases! Let me know if you want more advanced topics 🚀












Search

Reason

ChatGPT can make mistakes. Check important info.