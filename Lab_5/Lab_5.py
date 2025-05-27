def matrix_multiply(A, B):
    """
    Умножение матриц A и B
    Возвращает матрицу-произведение или None, если умножение невозможно
    """
    # Проверка на пустые матрицы
    if not A or not B:
        print("Ошибка: одна из матриц пустая")
        return None

    # Проверка возможности умножения
    cols_A = len(A[0])
    rows_B = len(B)

    if cols_A != rows_B:
        print(f"Ошибка: невозможно умножить ({len(A)}×{cols_A}) на ({rows_B}×{len(B[0])})")
        return None

    # Проверка согласованности размеров
    for row in A:
        if len(row) != cols_A:
            print("Ошибка: несоответствие размеров в матрице A")
            return None

    for row in B:
        if len(row) != len(B[0]):
            print("Ошибка: несоответствие размеров в матрице B")
            return None

    # Создание результирующей матрицы
    m = len(A)
    n = len(B[0])
    C = [[0.0 for _ in range(n)] for _ in range(m)]

    # Транспонируем B для более эффективного доступа по столбцам
    B_transposed = list(zip(*B))

    # Вычисление произведения с оптимизированным доступом
    for i in range(m):
        for j in range(n):
            # Используем sum и генератор для вычисления скалярного произведения
            C[i][j] = sum(A[i][k] * B_transposed[j][k] for k in range(cols_A))

    return C


def input_matrix(name):
    """Ввод матрицы с клавиатуры"""
    while True:
        try:
            rows = int(input(f"Введите количество строк матрицы {name}: "))
            cols = int(input(f"Введите количество столбцов матрицы {name}: "))
            if rows <= 0 or cols <= 0:
                print("Размеры должны быть положительными числами!")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число!")

    print(f"Введите элементы матрицы {name} построчно (через пробел):")
    matrix = []
    for i in range(rows):
        while True:
            row = input(f"Строка {i + 1}: ").strip().split()
            if len(row) != cols:
                print(f"Ошибка: ожидается {cols} элементов, получено {len(row)}")
                continue

            try:
                matrix.append([float(x) for x in row])
                break
            except ValueError:
                print("Ошибка: все элементы должны быть числами!")

    return matrix


def print_matrix(matrix, name, width=10):
    """Вывод матрицы на экран с форматированием"""
    if not matrix:
        print(f"\nМатрица {name}: [пустая]")
        return

    print(f"\nМатрица {name} ({len(matrix)}×{len(matrix[0])}):")
    for row in matrix:
        formatted_row = [f"{x:{width}.4f}" if isinstance(x, (int, float)) else f"{x:^{width}}" for x in row]
        print(" ".join(formatted_row))


def main():
    print("Программа умножения матриц A(m×n) и B(n×l)")

    try:
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

    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {str(e)}")


if __name__ == "__main__":
    main()