matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

filtered_list = [element for row in matrix for element in row if element % 2 == 0]
print(filtered_list)

print('-------------------------second example 👇----------------------')

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed_matrix)




for i in range(len(matrix[0])):  
    new_row = [row[i] for row in matrix]
    print(f"Column {i} → {new_row}")
"""
row is not the whole matrix—it's just one row at a time.
row[i] extracts a single element from each row.
[
    [1, 4, 7, 10, 13],  # First column → First row
    [2, 5, 8, 11, 14],  # Second column → Second row
    [3, 6, 9, 12, 15]   # Third column → Third row
]
"""