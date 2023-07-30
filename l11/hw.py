class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        rows = [' '.join(str(elem) for elem in row) for row in self.data]
        return '\n'.join(rows)

    def __eq__(self, other):
        return self.data == other.data

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrix dimensions are not compatible for addition.")
        
        result = []
        for i in range(len(self.data)):
            row = [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
            result.append(row)
        
        return Matrix(result)

    def __mul__(self, other):
        if len(self.data[0]) != len(other.data):
            raise ValueError("Matrix dimensions are not compatible for multiplication.")
        
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(other.data[0])):
                val = sum(self.data[i][k] * other.data[k][j] for k in range(len(self.data[0])))
                row.append(val)
            result.append(row)

        return Matrix(result)


# Example usage
matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix 1 == Matrix 2?", matrix1 == matrix2)  # Output: False

matrix_sum = matrix1 + matrix2
print("\nMatrix 1 + Matrix 2:")
print(matrix_sum)

matrix_product = matrix1 * matrix2
print("\nMatrix 1 * Matrix 2:")
print(matrix_product)
