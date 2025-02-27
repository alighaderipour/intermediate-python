"""
🔹 2️⃣ Decorators (Modifying Function Behavior Dynamically)
🧠 Concept Overview

    Why use decorators?
        They modify functions without changing their actual code
        Useful for logging, authentication, caching, validation, etc.
"""

"""
🔹 Intermediate Example: A Permission System

💡 Scenario: We need a decorator that checks if a user is an admin before executing a function.

"""
def admin_required(func):
    def wrapper(user_role, *args, **kwargs):
        if user_role != "admin":
            raise PermissionError("Access denied: Admins only!")
        return func(*args, **kwargs)
    return wrapper

@admin_required
def delete_user(username):
    print(f"User {username} has been deleted.")

delete_user("admin", "john_doe")  # ✅ Allowed
# delete_user("user", "john_doe")  # ❌ Raises PermissionError

"""
🧐 Key Takeaways:
✔ Reusability – Can be applied to multiple functions.
✔ Separation of Concerns – Function remains clean, logic stays in decorator.
"""