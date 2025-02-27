# Sometimes, we need a property that automatically enforces formatting rules.
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".title()  # Always formatted properly

    @full_name.setter
    def full_name(self, new_name):
        first, last = new_name.split()
        self.first_name = first
        self.last_name = last

e = Employee("john", "doe")
print(e.full_name)  # ✅ John Doe (Auto-formatted)
e.full_name = "jane smith"
print(e.first_name, e.last_name)  # ✅ Jane Smith (Auto-update both attributes)

"""
🔹 What’s happening?

    full_name always returns a properly formatted string.
    If you update full_name, it automatically updates first_name and last_name.

"""