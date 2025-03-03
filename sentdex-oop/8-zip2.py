"""
1. Basic Usage: Pairing Two Lists
Suppose you have two lists and want to pair their elements together.
"""

list1 = [1, 2, 3]
list2 = ["True", "False"]
combined_lists = list(zip(list1, list2))
print(combined_lists)


"""
2. Iterating Over Multiple Sequences Simultaneously
You can use zip() in a for loop to iterate over multiple sequences at once.
"""
persons = ["Ali", "Reza"]
ages = [13, 54]
for person, age in zip(persons, ages):
    print("{} is {}".format(person, age))

"""
3. Unzipping Data
If you have zipped data and want to separate it back into individual lists, 
you can use the unpacking operator *.
"""
zipped_data = [("Ali", 21 , "Male"), ("Zahra", 33, "Female"), ("Razieh", 16, "Female")]
names, ages, sexes = zip(*zipped_data)
print(names)
print(ages)
print(sexes)


"""
6. Transposing a Matrix
zip() can be used to transpose a matrix (swap rows and columns).
"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose_matrix = list(zip(*matrix))
print(transpose_matrix)


# or 
tr = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(tr)