def create_matrix(row,columns):
    matrix = []
    for i in range(row):
        row = []
        for j in range(columns):
            element = float(input(f"Enter element for row {i + 1}, column {j +1}: "))
            row.append(element)
        matrix.append(row)
    return matrix
result_matrix = create_matrix(2, 2)
print("Created Matrix:")
for row in result_matrix:
    print(row)