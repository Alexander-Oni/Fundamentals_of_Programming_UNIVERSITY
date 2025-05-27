def matrix_multiply(A, B):
    """
    Умножение матриц A и B
    Возвращает матрицу-произведение или None, если умножение невозможно
    """
    # Проверка возможности умножения
    if len(A[0]) != len(B):
        print("Ошибка: количество столбцов матрицы A не равно количеству строк матрицы B")
        return None

    # Создание результирующей матрицы
    m = len(A)  # Количество строк матрицы A
    n = len(B[0])  # Количество столбцов матрицы B
    C = [[0 for _ in range(n)] for _ in range(m)]

    # Вычисление произведения
    for i in range(m):
        for k in range(n):
            # Вычисление элемента c_ik
            c_ik = 0
            for j in range(len(A[0])):
                c_ik += A[i][j] * B[j][k]
            C[i][k] = c_ik

    return C


def input_matrix(name):
    """Ввод матрицы с клавиатуры"""
    rows = int(input(f"Введите количество строк матрицы {name}: "))
    cols = int(input(f"Введите количество столбцов матрицы {name}: "))

    print(f"Введите элементы матрицы {name} построчно (через пробел):")
    matrix = []
    for i in range(rows):
        while True:
            row = input(f"Строка {i + 1}: ").split()
            if len(row) == cols:
                try:
                    matrix.append([float(x) for x in row])
                    break
                except ValueError:
                    print("Ошибка: введите числа!")
            else:
                print(f"Ошибка: введите ровно {cols} элементов!")

    return matrix


def print_matrix(matrix, name):
    """Вывод матрицы на экран"""
    print(f"\nМатрица {name}:")
    for row in matrix:
        print(" ".join(f"{x:8.2f}" for x in row))


# Основная программа
print("Программа умножения матриц A(m×n) и B(n×l)")

# Ввод матриц
A = input_matrix("A")
B = input_matrix("B")

# Умножение матриц
C = matrix_multiply(A, B)

# Вывод результата
if C is not None:
    print_matrix(A, "A")
    print_matrix(B, "B")
    print_matrix(C, "C = A×B")