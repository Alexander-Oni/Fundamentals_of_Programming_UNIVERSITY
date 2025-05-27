from random import uniform

# Функция для создания массива
def create_array(n):
    # Создаем массив из n случайных чисел от -10 до 10
    return [uniform(-10, 10) for _ in range(n)]


# Функция для вычислений
def calculate(arr, y):
    # Проверяем корректность y
    if not (min(arr) < y < max(arr)):
        raise ValueError("Значение y должно быть между минимальным и максимальным элементами массива")

    # Инициализируем переменные для вычислений
    product = 1  # произведение
    sum_modules = 0  # сумма модулей

    # Проходим по всем элементам массива
    for num in arr:
        # Если модуль числа больше y - умножаем на произведение
        if abs(num) > y:
            product *= num
        # Иначе добавляем модуль числа к сумме
        else:
            sum_modules += abs(num)

    return product, sum_modules


# Основная программа
def main():
    # Ввод данных
    n = int(input("Введите размер массива n: "))
    y = float(input("Введите число y: "))

    # Создаем массив
    array = create_array(n)

    # Выводим созданный массив
    print("Созданный массив:", array)

    try:
        # Вычисляем значения
        prod, summ = calculate(array, y)

        # Выводим результаты
        print(f"Произведение элементов с модулем > {y}: {prod}")
        print(f"Сумма модулей остальных элементов: {summ}")
    except ValueError as e:
        print("Ошибка:", e)

# Запуск программы
if __name__ == "__main__":
    main()
