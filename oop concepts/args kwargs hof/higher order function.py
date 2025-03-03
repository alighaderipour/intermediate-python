Higher-order functions (HOFs) in Python are functions that either:

Take one or more functions as arguments.
Return a function as a result.
They enable powerful programming techniques like function composition, callbacks, and decorators.

🔹 Beginner Examples (Covering the Basics)
Example 1: Functions as Arguments (Using map)
A function can accept another function as an argument.

python
Copy
Edit
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]

# Passing `square` function as an argument to `map`
squared_numbers = list(map(square, numbers))

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
✅ Key Concept: map() is a higher-order function because it takes another function (square) as an argument.

Example 2: Functions Returning Functions
A function can return another function.

python
Copy
Edit
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)  # Returns the inner function `multiply`
triple = multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
✅ Key Concept: multiplier(2) returns a function that multiplies any number by 2.

Example 3: Using filter()
The filter() function takes another function as an argument and filters a list based on a condition.

python
Copy
Edit
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))

print(even_numbers)  # Output: [2, 4, 6]
✅ Key Concept: filter() is a higher-order function because it takes a function (is_even) as an argument.

🔹 Intermediate Examples
Example 4: Using reduce() for Aggregation
The reduce() function applies a function cumulatively to the elements of a list.

python
Copy
Edit
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(add, numbers)

print(sum_numbers)  # Output: 15
✅ Key Concept: reduce() applies add() sequentially: ((1+2)+3)+4)+5).

Example 5: Function Composition
You can combine multiple functions dynamically.

python
Copy
Edit
def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

def compose(f, g):
    return lambda x: f(g(x))

new_function = compose(add_one, multiply_by_two)

print(new_function(3))  # Output: (3 * 2) + 1 = 7
✅ Key Concept: compose() returns a function that applies g first and then f.

🔹 Practical Use Cases of Decorators
Example 6: Logging Decorator
A decorator is a function that wraps another function, adding functionality without modifying the original function.

python
Copy
Edit
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

print(add(2, 3))
✅ Key Concept: @log_function_call automatically logs function calls.

Example 7: Timing Execution
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
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)

slow_function()
✅ Key Concept: @timer measures execution time of the decorated function.

🔹 Advanced Decorator Use Cases
Example 8: A Decorator with Arguments
Decorators can accept arguments by adding another level of nesting.

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

@repeat(3)  # Calls the function 3 times
def say_hello():
    print("Hello!")

say_hello()
✅ Key Concept: The repeat(n) decorator allows customization of function behavior.

Example 9: Class-Based Decorator
You can implement decorators as classes.

python
Copy
Edit
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Function {self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
✅ Key Concept: The class stores the count and modifies function behavior dynamically.

🔥 Summary
Beginner
Functions as arguments (map)
Functions returning functions
Using filter()
Intermediate
Using reduce()
Function composition
Practical Decorators
Logging function calls
Measuring execution time
Advanced Decorators
Decorators with arguments
Class-based decorators
Would you like me to explain any part in more detail? 🚀
