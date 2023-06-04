def add_matrices(matrix1, matrix2):

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            sum_element = matrix1[i][j] + matrix2[i][j]
            row.append(sum_element)
        result.append(row)
    
    return result
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[0, 0, 0], [2, 2, 2], [3, 3, 3]]
result_matrix = add_matrices(matrix1, matrix2)
print(result_matrix)
