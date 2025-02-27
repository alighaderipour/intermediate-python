"""
🔹 1️⃣ property (Encapsulation & Controlled Attribute Access)
🧠 Concept Overview

    Why use property?
        Controls attribute access (read/write restrictions)
        Applies data validation when setting values
        Allows computed properties (like full_name)

Think of property as a smart variable—it looks like an attribute, but it actually executes a method!
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Internal attribute

    @property
    def salary(self):
        """Getter for salary"""
        return self._salary

    @salary.setter
    def salary(self, value):
        """Setter with validation"""
        if not (30000 <= value <= 200000):
            raise ValueError("Salary must be between $30,000 and $200,000.")
        self._salary = value  # Update only if valid

emp = Employee("Alice", 50000)
print(emp.salary)  # ✅ 50000

emp.salary = 120000  # ✅ Allowed
# emp.salary = 250000  # ❌ Raises ValueError
"""
🧐 Key Takeaways:
✔ Protects salary constraints automatically.
✔ Raises an error for invalid assignments.
✔ Prevents accidental bad data from creeping into the system.
"""