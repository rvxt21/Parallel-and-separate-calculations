
class CustomRandomGenerator:
    def __init__(self, seed=0):
        self.seed = seed

    def next(self):
        self.seed = (self.seed * 1664525 + 1013904223) & 0xFFFFFFFF
        return self.seed

    def randint(self, min_value, max_value):
        random_value = self.next()
        return min_value + random_value % (max_value - min_value + 1)


class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[0 for _ in range(columns)] for _ in range(rows)]

    def fill_the_matrix_with_input(self):
        """
        Заповнення матриці вводом чисел.
        """
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] = int(input(f"Введіть елемент матриці "
                                         f"({i+1}, {j+1}): "))

    def fill_the_matrix(self, custom_random: CustomRandomGenerator):
        """
        Заповнення матриці вводом чисел.
        """
        try:
            custom_random = CustomRandomGenerator(seed=42)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    self.matrix[i][j] = custom_random.randint(1, 10)
        except Exception as e:
            print(f'Сталась помилка при заповненні матриць: {e}')

    def print_matrix(self):
        """
        Друкуємо матрицю на екран
        """
        for row in self.matrix:
            print(row)

    @staticmethod
    def add_matrices(matrix1: 'Matrix', matrix2: 'Matrix') -> 'Matrix':
        try:
            if matrix1.rows != matrix2.rows or \
                    matrix1.columns != matrix2.columns:
                raise ValueError("Матриці мають бути однакового розміру!")

            result_matrix = Matrix(matrix1.rows, matrix1.columns)
            for i in range(result_matrix.rows):
                for j in range(result_matrix.columns):
                    result_matrix.matrix[i][j] = matrix1.matrix[i][j] + \
                                               matrix2.matrix[i][j]
                return result_matrix
        except Exception as e:
            print(f"Помилка під час додавання матриць: {e}")

    @staticmethod
    def multiply_matrices(matrix1: 'Matrix', matrix2: 'Matrix') -> 'Matrix':
        try:
            if matrix1.columns != matrix2.rows:
                raise ValueError(
                    "Кількість стовпців першої матриці повинна "
                    "дорівнювати кількості рядків другої матриці.")
            result_matrix = Matrix(matrix1.rows, matrix2.columns)
            for i in range(result_matrix.rows):
                for j in range(result_matrix.columns):
                    for k in range(matrix1.columns):
                        result_matrix.matrix[i][j] += matrix1.matrix[i][k] * \
                                                    matrix2.matrix[k][j]

            return result_matrix
        except Exception as e:
            print(f"Помилка під час множення матриць: {e}")


if __name__ == "__main__":
    print('*' * 100)
    print('Перша матриця:')
    n = int(input("Введіть кількість строк (m): "))
    m = int(input("Введіть кількість стовпців (n): "))
    matrix = Matrix(m, n)
    custom_random = CustomRandomGenerator(seed=42)
    matrix.fill_the_matrix(custom_random)
    print("Ваша матриця:")
    matrix.print_matrix()

    print('*' * 100)
    print('Друга матриця:')
    n = int(input("Введіть кількість строк (m): "))
    m = int(input("Введіть кількість стовпців (n): "))
    matrix_1 = Matrix(m, n)
    matrix_1.fill_the_matrix(custom_random)
    print("Ваша 2 матриця:")
    matrix_1.print_matrix()

    print('*' * 100)
    print('Сума двох матриць')
    result_add_matrix = Matrix.add_matrices(matrix, matrix_1)
    result_add_matrix.print_matrix()

    print('*' * 100)
    print('Множення двох матриць')
    result_multiply_matrix = Matrix.multiply_matrices(matrix, matrix_1)
    result_multiply_matrix.print_matrix()