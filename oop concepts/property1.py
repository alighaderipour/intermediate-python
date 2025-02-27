"""
property is a built-in function that allows you to control access to instance attributes
in an object-oriented way. 
It helps in encapsulation by defining getters, setters, and deleters for an attribute
while still using dot notation.
"""
class Person:
    def __init__(self, name):
        self._name = name  # Private attribute (conventionally)

    @property
    def name(self):  # Getter
        return self._name

p = Person("Alice")
print(p.name)  # ✅ Allowed: Accessing name
# p.name = "Bob"  # ❌ Error: Cannot modify a read-only property
