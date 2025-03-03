What Are Generators in Python?
A generator in Python is a special type of iterator that allows you to iterate over a sequence of values lazily, meaning it generates values on demand rather than storing them in memory. Unlike lists, which hold all their elements in memory at once, generators produce items one at a time and only when needed.

Key Features of Generators
Memory Efficient – They don’t store all elements in memory but generate them dynamically.
Lazy Evaluation – Values are produced only when requested.
Maintains State – They remember where they left off between calls.
Used for Streaming Data – Ideal for handling large datasets.
How Are Generators Created?
There are two ways to create generators:

Using yield in a function
Using generator expressions (like list comprehensions but with parentheses)
1️⃣ Basics of Generators
Let's start with three basic examples.

Example 1: A Simple Generator
python
Copy
Edit
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
Explanation:
The function simple_generator contains yield statements instead of return.
yield pauses the function and returns a value, but remembers where it left off.
next(gen) resumes execution from the last yield and continues.
Example 2: Generating a Range of Numbers (Like range())
python
Copy
Edit
def number_generator(n):
    for i in range(n):
        yield i

gen = number_generator(5)
print(list(gen))  # Output: [0, 1, 2, 3, 4]
Explanation:
This generator mimics the behavior of Python’s range() function.
Instead of storing n elements in a list, it yields them one at a time.
Example 3: Infinite Generator
python
Copy
Edit
def infinite_counter():
    n = 0
    while True:
        yield n
        n += 1

gen = infinite_counter()
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
Explanation:
This generator runs forever unless stopped (Ctrl + C or using break).
This is useful in real-world applications like log monitoring, stream processing, etc.
2️⃣ Intermediate Generator Examples
Example 4: Fibonacci Sequence Generator
python
Copy
Edit
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for _ in range(10):
    print(next(gen), end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34
Explanation:
This efficiently generates the Fibonacci sequence.
Each call to next() generates the next Fibonacci number without storing the entire sequence.
Example 5: Reading a Large File Line by Line
python
Copy
Edit
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

for line in read_large_file('large_text.txt'):
    print(line)  # Prints lines one by one without loading the whole file into memory.
Why is this Useful?
If you have a very large file, reading it all at once would consume a lot of RAM.
Using a generator, each line is read only when needed.
Example 6: Generator Expression (Like List Comprehension)
python
Copy
Edit
gen = (x**2 for x in range(5))
print(list(gen))  # Output: [0, 1, 4, 9, 16]
Explanation:
Instead of [x**2 for x in range(5)], which stores all values in memory, this generates values lazily.
3️⃣ Advanced Generator Examples
Example 7: Two-Way Communication (send())
python
Copy
Edit
def interactive_generator():
    while True:
        value = yield
        print(f"Received: {value}")

gen = interactive_generator()
next(gen)  # Move to the first yield
gen.send("Hello")  # Output: Received: Hello
gen.send("World")  # Output: Received: World
Explanation:
Unlike next(), which only retrieves values, send() injects a value into the generator.
Used in coroutines and cooperative multitasking.
Example 8: Chaining Generators
python
Copy
Edit
def squares(n):
    for i in range(n):
        yield i * i

def double_squares(n):
    for val in squares(n):
        yield val * 2

print(list(double_squares(5)))  # Output: [0, 2, 8, 18, 32]
Explanation:
We create a chain of generators that process values step by step.
This is useful in data pipelines.
4️⃣ Practical Generator Use Cases
Example 9: Implementing Pagination
python
Copy
Edit
def paginate(iterable, page_size):
    page = []
    for item in iterable:
        page.append(item)
        if len(page) == page_size:
            yield page
            page = []
    if page:
        yield page  # Yield remaining items

data = range(15)  
for page in paginate(data, 5):
    print(page)
# Output: [0, 1, 2, 3, 4]
#         [5, 6, 7, 8, 9]
#         [10, 11, 12, 13, 14]
Why use generators?
Instead of returning a massive list, we fetch data page by page, reducing memory usage.
Example 10: Streaming API Requests
python
Copy
Edit
import requests

def fetch_data(api_url):
    while api_url:
        response = requests.get(api_url).json()
        yield response['data']
        api_url = response.get('next_page_url')  # Get next page URL

for data in fetch_data("https://api.example.com/data"):
    print(data)  # Each iteration fetches and processes a chunk of data.
Why?
We don’t load all API data at once, reducing memory consumption.
Example 11: Simulating Data Streams
python
Copy
Edit
import random
import time

def live_sensor_data():
    while True:
        yield random.uniform(20.0, 30.0)  # Simulated temperature reading
        time.sleep(1)  # Simulate delay

for reading in live_sensor_data():
    print(f"Temperature: {reading:.2f}°C")
Use Case:
Real-time sensor data, stock market prices, etc.
Example 12: Batched Processing
python
Copy
Edit
def batch_process(iterable, batch_size):
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch

for batch in batch_process(range(10), 3):
    print(batch)  # Output: [0, 1, 2], [3, 4, 5], [6, 7, 8], [9]
Why?
Efficient for batch processing in ML pipelines.
Conclusion
Generators make Python memory-efficient and fast. Mastering them will help you handle large datasets, real-time streams, and lazy evaluations effectively. 🚀












Search

Reason

ChatGPT can make mistakes. Check important info.
