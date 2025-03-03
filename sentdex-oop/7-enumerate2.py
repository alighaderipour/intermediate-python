"""
🔹 Intermediate Examples
These examples showcase slightly deeper concepts that go beyond basic enumeration.

1️⃣ Keeping Track of Indices While Filtering
This example filters even numbers while keeping track of their original indices

"""

numbers = [10, 25, 32, 47, 50, 66]

filtered_indices = [(i, num) for i, num in enumerate(numbers) if num % 2 == 0]

print(filtered_indices)
"""
🔹 Why is this useful?
Instead of looping separately to find indices, 
we use enumerate to keep track of both the number and its position in one step.

"""

"""
2️⃣ Enumerate with a Custom Start Index
Often, you need a custom starting index when working with sequences.

"""
tasks = ["Write report", "Fix bug", "Deploy app"]

for idx, task in enumerate(tasks, start=101):  # Custom numbering
    print(f"Task {idx}: {task}")
"""
🔹 Why is this useful?
This is helpful when dealing with databases, task tracking, or IDs that don’t start from zero.

"""
"""
🔹 Practical Examples
These examples demonstrate how enumerate is useful in real-world programming.

3️⃣ Using Enumerate to Rename Files
If you need to rename files dynamically (e.g., when batch processing files in a directory):
"""
import os

files = ["document.txt", "image.png", "report.pdf"]

for i, file in enumerate(files, start=1):
    new_name = f"file_{i}_{file}"
    print(f"Renaming {file} to {new_name}")
    # os.rename(file, new_name)  # Uncomment this when working with real files
"""
🔹 Why is this useful?
Batch processing filenames is common in automation tasks.

"""

"""
4️⃣ Parallel Iteration of Two Lists
Using enumerate to iterate over two lists together without using zip.
"""
students = ["Alice", "Bob", "Charlie"]
grades = [85, 92, 78]

for i, student in enumerate(students):
    print(f"Student {student} (#{i+1}) got {grades[i]} marks.")
"""
🔹 Why is this useful?
It avoids extra loops and keeps index tracking simple when working with multiple lists.

"""