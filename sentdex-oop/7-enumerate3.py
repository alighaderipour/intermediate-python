"""
The enumerate function in Python is a powerful and commonly used tool, especially among experienced programmers. It simplifies iterating over sequences (like lists, tuples, or strings) by providing both the index and the value of each element. Below are practical examples of how top-level programmers use enumerate effectively in real-world scenarios.

1. Iterating Over a List with Indices
This is the most common use case for enumerate. Instead of manually managing an index variable, enumerate provides it automatically.

Example: Adding Line Numbers to Output
"""

lines = ["Python is fun", "Enumerate is useful", "Keep learning!"]

for index, line in enumerate(lines, start=1):
    print(f"{index}: {line}")


"""
2. Finding the Index of Specific Elements
When searching for specific elements in a list, enumerate makes it easy to retrieve their indices.

Example: Finding All Indices of a Target Value
"""

numbers = [10, 20, 30, 20, 40, 20]
target = 20

indices = [index for index, value in enumerate(numbers) if value == target]
print(indices)


"""
3. Processing Files with Line Numbers
When working with files, enumerate is often used to process lines while keeping track of line numbers.

Example: Printing Lines with Errors
"""
with open("data.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        if "ERROR" in line:
            print(f"Error found on line {line_number}: {line.strip()}")


"""
4. Creating Dictionaries from Lists
enumerate can be used to create dictionaries where the keys are indices or other derived values.

Example: Creating a Dictionary of Index-Value Pairs
"""
fruits = ["apple", "banana", "cherry"]

fruit_dict = {index: fruit for index, fruit in enumerate(fruits)}
print(fruit_dict)

"""
5. Combining enumerate with Other Functions
Top-level programmers often combine enumerate with functions like zip, filter, or map for more advanced use cases.

Example: Pairing Two Lists with Indices
"""

keys = ["a", "b", "c"]
values = [1, 2, 3]

paired = {key: (index, value) for index, (key, value) in enumerate(zip(keys, values))}
print(paired)



"""
6. Skipping or Selecting Specific Indices
enumerate is often used to skip or select specific indices during iteration.

Example: Skipping Every Other Element

"""
data = [10, 20, 30, 40, 50, 60]

selected = [value for index, value in enumerate(data) if index % 2 == 0]
print(selected)

"""
7. Using enumerate with Nested Loops
In nested loops, enumerate helps track indices at multiple levels.

Example: Printing a Matrix with Row and Column Indices
"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row_index, row in enumerate(matrix):
    for col_index, value in enumerate(row):
        print(f"Element at ({row_index}, {col_index}) is {value}")


"""
8. Efficiently Updating Lists
enumerate is often used to update lists in place based on their indices.

Example: Squaring Even-Indexed Elements
"""

numbers = [1, 2, 3, 4, 5, 6]

for index, value in enumerate(numbers):
    if index % 2 == 0:
        numbers[index] = value ** 2

print(numbers)

"""
9. Combining enumerate with enumerate
In some cases, you may need to use enumerate twice to process hierarchical data.

Example: Comparing Two Lists with Indices
"""
list1 = [10, 20, 30]
list2 = [15, 25, 35]

for index1, value1 in enumerate(list1):
    for index2, value2 in enumerate(list2):
        print(f"Comparing {value1} (index {index1}) with {value2} (index {index2})")


"""
10. Real-World Use Case: Logging Debug Information
enumerate is often used in logging to include context about the position of data being processed.

Example: Logging Progress in a Loop
"""
import logging

logging.basicConfig(level=logging.INFO)

items = ["task1", "task2", "task3"]

for index, item in enumerate(items, start=1):
    logging.info(f"Processing item {index}: {item}")

"""
Summary of Key Benefits of enumerate
Simplifies Code: Eliminates the need for manual index management.
Improves Readability: Makes the intent of the code clearer.
Enhances Efficiency: Combines iteration and indexing in a single step.
Versatile: Works seamlessly with lists, tuples, strings, files, and more.
"""