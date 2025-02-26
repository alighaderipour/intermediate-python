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