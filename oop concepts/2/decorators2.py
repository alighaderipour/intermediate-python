"""
 Practical Example: Logging Function Execution

💡 Scenario: We want to log every function execution automatically.

"""
import time

def log_execution(func):
    """Decorator to log function execution time"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@log_execution
def slow_function():
    time.sleep(2)
    print("Function completed!")

slow_function()
"""
🧐 Key Takeaways:
✔ Used in performance monitoring.
✔ Works without modifying the original function.
"""