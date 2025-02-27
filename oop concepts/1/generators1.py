"""
What is a Generator?

A generator is a function that remembers its state and can yield multiple values lazily without storing them all in memory. It is useful for working with large data streams.
"""

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

gen = count_up_to(5)
print(next(gen))  # ✅ 1
print(next(gen))  # ✅ 2
print(list(gen))  # ✅ [3, 4, 5]
