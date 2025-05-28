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

def read_matrices_from_file(filename):
    """Чтение двух матриц из файла input.txt"""
    try:
        with open(filename, 'r') as file:
            # Читаем первую матрицу
            matrix_A = []
            while True:
                line = file.readline().strip()
                if not line:  # Пустая строка между матрицами
                    break
                row = [float(x) for x in line.split()]
                matrix_A.append(row)

            # Читаем вторую матрицу
            matrix_B = []
            for line in file:
                row = [float(x) for x in line.strip().split()]
                matrix_B.append(row)

        return matrix_A, matrix_B

    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        return None, None
    except ValueError:
        print("Ошибка: все элементы должны быть числами!")
        return None, None

def write_matrices_to_file(filename, A, B, C):
    try:
        with open(filename, 'w', encoding='utf-8') as file:  # Добавляем параметр encoding
            # Записываем матрицу A
            file.write("Матрица A:\n")
            for row in A:
                file.write(' '.join(f"{x:.4f}" for x in row) + '\n')
            file.write("\n")

            # Записываем матрицу B
            file.write("Матрица B:\n")
            for row in B:
                file.write(' '.join(f"{x:.4f}" for x in row) + '\n')
            file.write("\n")

            # Записываем матрицу C
            file.write("Матрица C = A×B:\n")
            for row in C:
                file.write(' '.join(f"{x:.4f}" for x in row) + '\n')
    except IOError:
        print(f"Ошибка записи в файл {filename}")

def main():
    print("Программа умножения матриц A(m×n) и B(n×l)")

    try:
        # Чтение матриц из файла input.txt
        A, B = read_matrices_from_file('Файлы_для_пятой_лабы/input_data.txt')

        if A is None or B is None:
            return

        # Умножение матриц
        C = matrix_multiply(A, B)

        # Запись результата в файл output.txt
        if C is not None:
            write_matrices_to_file('Файлы_для_пятой_лабы/output_data.txt', A, B, C)
            print("Результат успешно записан в файл output.txt")

    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {str(e)}")

if __name__ == "__main__":
    if __name__ == "__main__":
        try:
            # Запускаем основную функцию программы
            main()
        except Exception as e:
            # Обработка общих ошибок
            print(f"Произошла непредвиденная ошибка: {str(e)}")
            print("Пожалуйста, проверьте формат входных данных в файле input.txt")
