Understanding property in Python
What is property in Python?
In Python, the property function is a built-in mechanism that allows you to define a managed attribute in a class. It lets you define getter, setter, and deleter methods for an attribute while still allowing attribute-style access instead of calling methods directly.

Essentially, property provides controlled access to class attributes while maintaining encapsulation and flexibility.

Why Use property?
Encapsulation: Helps manage attribute access while keeping an easy-to-use syntax.
Validation: Allows adding logic when setting an attribute (e.g., type checking or range validation).
Computed Properties: Allows dynamically calculating a value instead of storing it.
Read-only Attributes: Prevents modification of an attribute after it's set.
Backward Compatibility: Helps maintain a consistent API even when changing internal implementations.
Basic Syntax of property
There are two ways to define a property:

Using the property() function.
Using the @property decorator (preferred method).
Method 1: Using property()
python
Copy
Edit
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private attribute

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    def del_radius(self):
        print("Radius deleted")
        del self._radius

    radius = property(get_radius, set_radius, del_radius, "This is the radius property")
Explanation:
get_radius() → Acts as the getter.
set_radius() → Acts as the setter with validation.
del_radius() → Deletes the attribute.
property(get_radius, set_radius, del_radius, "Docstring") → Defines a property.
Method 2: Using @property Decorator (Preferred)
python
Copy
Edit
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Getter method"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter method"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @radius.deleter
    def radius(self):
        """Deleter method"""
        print("Radius deleted")
        del self._radius
Why is this preferred?
More readable: Clear separation of getter, setter, and deleter.
Less boilerplate: No need to use property() explicitly.
Encapsulation: The actual attribute (_radius) is hidden.
Examples of property
Basic Examples
1. Read-Only Property
python
Copy
Edit
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name  # No setter means it's read-only
Usage:

python
Copy
Edit
e = Employee("John", 50000)
print(e.name)  # John
e.name = "Mike"  # Error: AttributeError: can't set attribute
2. Property with Validation
python
Copy
Edit
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
Usage:

python
Copy
Edit
p = Person(25)
print(p.age)  # 25
p.age = -5  # Raises ValueError
3. Computed Property
python
Copy
Edit
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height  # Computed dynamically
Usage:

python
Copy
Edit
r = Rectangle(10, 5)
print(r.area)  # 50
r.width = 20
print(r.area)  # 100 (updates dynamically)
Intermediate Examples
4. Property with Dependent Attributes
python
Copy
Edit
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9
Usage:

python
Copy
Edit
temp = Temperature(25)
print(temp.fahrenheit)  # 77.0
temp.fahrenheit = 98.6
print(temp._celsius)  # 37.0
5. Lazy Evaluation with Caching
python
Copy
Edit
class Data:
    def __init__(self, value):
        self._value = value
        self._processed = None

    @property
    def processed(self):
        if self._processed is None:  # Compute only when accessed
            print("Processing data...")
            self._processed = self._value ** 2  # Expensive operation
        return self._processed
Usage:

python
Copy
Edit
d = Data(10)
print(d.processed)  # Computes and caches the value
print(d.processed)  # Uses cached value
6. Property with Resettable Cache
python
Copy
Edit
class User:
    def __init__(self, name):
        self._name = name
        self._hashed_password = None

    @property
    def hashed_password(self):
        if self._hashed_password is None:
            print("Hashing password...")
            self._hashed_password = hash(self._name)  # Simulating password hashing
        return self._hashed_password

    @hashed_password.deleter
    def hashed_password(self):
        print("Resetting password cache")
        self._hashed_password = None
Usage:

python
Copy
Edit
u = User("admin")
print(u.hashed_password)
del u.hashed_password  # Clears cache
print(u.hashed_password)  # Recomputes hash
Advanced Examples
7. Property with Dependency Tracking
python
Copy
Edit
class Account:
    def __init__(self, balance):
        self._balance = balance
        self._transactions = 0

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._transactions += 1
        self._balance = value
Usage:

python
Copy
Edit
a = Account(1000)
a.balance = 1200  # Tracks transactions
print(a._transactions)  # 1
8. Read-Only Singleton Property
python
Copy
Edit
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._api_key = "SECRET"
        return cls._instance

    @property
    def api_key(self):
        return self._api_key
Usage:

python
Copy
Edit
c1 = Config()
c2 = Config()
print(c1.api_key)  # SECRET
c1.api_key = "NEW_KEY"  # Error: AttributeError
These examples provide a full understanding of property in Python, from basics to advanced usage. Let me know if you need deeper explanations for any part!

Next, do you want me to cover generators now, following the same structured approach?












Search

Reason