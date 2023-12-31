def transpose_matrix(matrix):
    # Определяем количество строк и столбцов в матрице
    rows = len(matrix)
    cols = len(matrix[0])

    # Создаем новую матрицу с транспонированными размерами
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    # Заполняем новую матрицу значениями из исходной матрицы
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


# Исходная матрица
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Транспонированная матрица
transposed = transpose_matrix(matrix)

# Вывод результатов
print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nТранспонированная матрица:")
for row in transposed:
    print(row)
