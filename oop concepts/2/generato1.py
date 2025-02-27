1️⃣ property - Encapsulation in Python
🧠 Concept Overview:

    Why Use property?
        You can have attributes that behave like functions, with control over their get and set behavior.
        You can use property to encapsulate logic in your classes, such as performing validation, computation, or format changes when accessing or setting values.

🔹 Intermediate Example: A Rectangle with Lazy Area Calculation

Scenario:
You have a Rectangle class. You want to calculate the area lazily (only when requested), but you don’t want the user to directly modify the area—it’s derived from width and height.

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive!")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive!")
        self._height = value

    @property
    def area(self):
        """Lazy computed property"""
        return self._width * self._height

# Testing the class
rect = Rectangle(10, 5)
print(f"Area: {rect.area}")  # Area is calculated lazily: 50
rect.width = 15  # Changing the width
print(f"Updated Area: {rect.area}")  # Re-calculates area lazily: 75

Explanation:

    width and height have setter and getter methods to validate input.
    area is a lazy property: It doesn’t store the area but calculates it only when needed. This is more efficient if the area is often re-calculated and not directly stored.

🔹 Practical Example: Temperature Converter with Property

Scenario:
You want to manage temperatures in Celsius, but also allow getting and setting the temperature in Fahrenheit. The two units should be linked and the conversion should happen automatically when either one is set.

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit"""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature using Fahrenheit"""
        self._celsius = (value - 32) * 5/9

# Test case
temp = Temperature(25)
print(f"Temperature in Fahrenheit: {temp.fahrenheit}")  # 77.0

temp.fahrenheit = 100  # Set Fahrenheit, automatically adjusts Celsius
print(f"Updated Temperature in Celsius: {temp.celsius}")  # 37.777...

Explanation:

    Here, celsius is the primary attribute, but we have the fahrenheit property that automatically converts to Celsius whenever it’s set, ensuring that both are always in sync.

2️⃣ Decorators - Dynamic Function Enhancement
🧠 Concept Overview:

    Why use Decorators?
        They allow modular behavior modification: You can add pre- or post-processing logic to functions without modifying their core code. This makes your code more maintainable and readable.

🔹 Intermediate Example: Caching Decorator (Memoization)

Scenario:
You have a function that calculates Fibonacci numbers. Using memoization, you can cache previously computed results to avoid redundant calculations.

def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test case
print(fibonacci(10))  # 55
print(fibonacci(50))  # This is fast due to caching

Explanation:

    The memoize decorator caches function results. If a value is computed once, it’s stored, and subsequent calls for the same input use the cached value.

🔹 Practical Example: Authorization Decorator for Web Apps

Scenario:
In a web application, you need a decorator to check if the user has the correct permission to access certain pages.

def requires_permission(permission):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if permission not in user.permissions:
                raise PermissionError("Access denied!")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

# Example user object
class User:
    def __init__(self, permissions):
        self.permissions = permissions

@requires_permission("admin")
def access_admin_panel(user):
    print("Welcome to the admin panel!")

# Test case
admin_user = User(["admin", "user"])
access_admin_panel(admin_user)  # ✅ Welcome to the admin panel!

regular_user = User(["user"])
# access_admin_panel(regular_user)  # ❌ Raises PermissionError: Access denied!

Explanation:

    The requires_permission decorator checks the user's permissions before calling the original function. If the user doesn’t have the necessary permission, an exception is raised.
    This is common in web apps to manage user roles and access control.

3️⃣ Generators - Efficient Lazy Evaluation
🧠 Concept Overview:

    Why use Generators?
        Generators are used to lazily iterate over large data sets or streams. Instead of storing all values in memory, a generator yields one value at a time, making it memory efficient.

🔹 Intermediate Example: Infinite Data Stream (Lazy Fibonacci Generator)

Scenario:
You need to generate Fibonacci numbers, but you don’t know how many numbers you will need in advance. You want an infinite sequence that you can keep accessing lazily.

def infinite_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Test case
fib_gen = infinite_fibonacci()
for _ in range(10):
    print(next(fib_gen))  # Prints first 10 Fibonacci numbers

Explanation:

    This is an infinite generator: It generates Fibonacci numbers indefinitely without storing them in memory.
    It only computes the next number when needed via next(), making it memory efficient for large or infinite data.

🔹 Practical Example: Reading Large Files Efficiently

Scenario:
You need to process a massive text file but don’t want to load it entirely into memory.

def read_large_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()  # Yield one line at a time

# Test case: processing each line of a large file
for line in read_large_file("large_file.txt"):
    process(line)  # Only processes one line at a time

Explanation:

    This generator yields one line at a time from the file, ensuring that you never load the entire file into memory.
    It’s ideal for processing large files or data streams.

📝 Summary
Concept	What It Solves	Use Case	Example
property	Encloses logic for attribute access	Lazy computation, validation, format control	Temperature Converter
Decorators	Modifies or enhances function behavior	Caching, access control, logging	Memoization, Auth Decorator
Generators	Efficiently handles large datasets	Large file reading, infinite sequences	Fibonacci Generator, Large File Reader