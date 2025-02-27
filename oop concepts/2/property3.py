"""
🔹 Practical Example: Immutable ID for a User

💡 Scenario:

    Every user has a unique ID that cannot be changed after creation.
    Other attributes (like username) should be modifiable.
"""

import uuid

class User:
    def __init__(self, username):
        self.username = username
        self._user_id = uuid.uuid4()  # Generate unique ID at creation

    @property
    def user_id(self):
        """Read-only property"""
        return self._user_id

    def change_username(self, new_name):
        self.username = new_name

user = User("john_doe")
print(user.username)  # ✅ john_doe
print(user.user_id)   # ✅ Unique ID

user.change_username("jane_doe")  # ✅ Allowed
# user.user_id = "12345"  # ❌ Raises AttributeError
"""
🧐 Key Takeaways:
✔ user_id is read-only after creation.
✔ Ensures data integrity (No one can tamper with the ID).
"""