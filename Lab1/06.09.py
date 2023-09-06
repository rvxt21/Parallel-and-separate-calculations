from typing import List


class CustomRandomGenerator:
    def __init__(self, seed=0):
        self.seed = seed

    def next(self):
        self.seed = (self.seed * 1664525 + 1013904223) & 0xFFFFFFFF
        return self.seed

    def randint(self, min_value, max_value):
        random_value = self.next()
        return min_value + random_value % (max_value - min_value + 1)


def create_matrix(n: int, m: int) -> List[List[int]]:
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    return matrix


def fill_the_matrix_with_input(matrix: List[List[int]]) -> None:
    """
    Заповнення матриці вводом чисел.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = int(input(f"Введіть елемент матриці "
                                     f"({i+1}, {j+1}): "))


def fill_the_matrix(matrix: List[List[int]]) -> None:
    """
    Заповнення матриці вводом чисел.
    """
    try:
        custom_random = CustomRandomGenerator(seed=42)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = random_number = custom_random.randint(1, 10)
    except Exception as e:
        print(f'Сталась помилка при заповненні матриць: {e}')


def print_matrix(matrix: List[List[int]]):
    """
    Друкуємо матрицю на екран
    """
    for row in matrix:
        print(row)


def add_matrix(matrix1: List[List[int]],
               matrix2: List[List[int]]) -> List[List[int]]:
    try:
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("Матриці мають бути однакового розміру!")

        sum_matrix = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1)):
                sum_element = matrix1[i][j] + matrix2[i][j]
                row.append(sum_element)
            sum_matrix.append(row)

        return sum_matrix
    except Exception as e:
        print(f"Помилка під час додавання матриць: {e}")


def multiply_matrix(matrix1: List[List[int]],
                    matrix2: List[List[int]]) ->List[List[int]]:
    try:
        if len(matrix1[0]) != len(matrix2):
            raise ValueError(
                "Кількість стовпців першої матриці повинна "
                "дорівнювати кількості рядків другої матриці.")
        rows = len(matrix1)
        columns = len(matrix2[0])
        result_matrix = [[0 for _ in range(columns)] for _ in range(rows)]

        for i in range(rows):
            for j in range(columns):
                for k in range(len(matrix1[0])):
                    result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

        return result_matrix
    except Exception as e:
        print(f"Помилка під час множення матриць: {e}")


if __name__ == "__main__":

    print('*'*100)
    print('Перша матриця:')

    n = int(input("Введіть кількість строк (m): "))
    m = int(input("Введіть кількість столбців (n): "))

    matrix = create_matrix(m, n)
    fill_the_matrix(matrix)
    print("Ваша матриця:")
    print_matrix(matrix)

    print('*' * 100)
    print('Друга матриця:')

    n = int(input("Введіть кількість строк (m): "))
    m = int(input("Введіть кількість столбців (n): "))

    matrix_1 = create_matrix(m,n)
    fill_the_matrix(matrix_1)
    print("Ваша 2 матриця:")
    print_matrix(matrix_1)

    print('*' * 100)
    print('Сума двох матриць')

    sum_res = add_matrix(matrix, matrix_1)
    print(print_matrix(sum_res))

    print('*' * 100)
    print('Множення двох матриць')

    multiply_res = multiply_matrix(matrix, matrix_1)
    print(print_matrix(multiply_res))
