from random import uniform
import sys

def create_array(n):
    """Создает массив из n случайных чисел от -10 до 10"""
    return [round(uniform(-10, 10), 2) for _ in range(n)]  # Округляем до 2 знаков для читаемости

def calculate(arr, y):
    """Вычисляет произведение и сумму модулей с проверкой корректности y"""
    if not (min(arr) < y < max(arr)):
        raise ValueError(f"y={y} должно быть между {min(arr)} и {max(arr)}")

    product = 1
    sum_modules = 0

    for num in arr:
        if abs(num) > y:
            product *= num
        else:
            sum_modules += abs(num)

    return round(product, 4), round(sum_modules, 4)  # Округляем результаты

def process_file(input_file, output_file):
    """Обрабатывает данные из файла и записывает результаты"""
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            # Читаем все строки, игнорируя пустые
            lines = [line.strip() for line in infile if line.strip()]

            if len(lines) < 2:
                raise ValueError("Файл должен содержать минимум 2 строки (n и y)")

            try:
                n = int(lines[0])
                y = float(lines[1])
            except (ValueError, IndexError) as e:
                raise ValueError(f"Ошибка формата данных: {e}")

            # Генерация массива
            arr = create_array(n)

            # Запись исходных данных
            outfile.write(f"Исходные данные:\n")
            outfile.write(f"n = {n}\n")
            outfile.write(f"y = {y}\n")
            outfile.write(f"Сгенерированный массив:\n{arr}\n\n")

            try:
                # Вычисления
                product, sum_modules = calculate(arr, y)

                # Запись результатов
                outfile.write("Результаты:\n")
                outfile.write(f"1. Произведение элементов с модулем > {y}: {product}\n")
                outfile.write(f"2. Сумма модулей остальных элементов: {sum_modules}\n")
            except ValueError as e:
                outfile.write(f"Ошибка вычислений: {e}\n")

    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден!", file=sys.stderr)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}", file=sys.stderr)

if __name__ == "__main__":
    input_filename = 'Файлы_для_четвертой_лабы/input_data.txt'
    output_filename = 'Файлы_для_четвертой_лабы/output_data.txt'

    process_file(input_filename, output_filename)
    print(f"Обработка завершена. Результаты сохранены в {output_filename}")