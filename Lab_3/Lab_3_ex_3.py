from math import fabs

def taylor_series(x, epsilon):
    """Вычисление (1-x)^(-4) с помощью ряда Тейлора"""
    if fabs(x) >= 1:
        return float('nan'), 0

    result = 1.0  # Первый член ряда (1)
    n = 1  # Номер текущего члена
    term = 4 * x  # Второй член ряда (4x)
    total_terms = 2  # Уже учли два члена

    if fabs(term) < epsilon:
        return result, 1

    result += term

    while True:
        n += 1
        # Рекуррентная формула для следующего члена:
        term *= x * (n + 3) / n
        result += term
        total_terms += 1

        if fabs(term) < epsilon:
            break

    return result, total_terms


def exact_value(x):
    """Точное значение функции (1-x)^(-4)"""
    return (1 - x) ** (-4) if fabs(x) < 1 else float('nan')


# Ввод параметров
print("Вычисление функции (1-x)^(-4) с помощью ряда Тейлора")
print("Ряд: (1-x)^(-4) = 1 + 4x + 10x² + 20x³ + 35x⁴ + ...")
xb = float(input("Введите Xbeg (|x| < 1): "))
xe = float(input("Введите Xend (|x| < 1): "))
dx = float(input("Введите шаг Dx: "))
epsilon = float(input("Введите точность ε: "))

# Проверка корректности ввода
if fabs(xb) >= 1 or fabs(xe) >= 1:
    print("Ошибка: |x| должен быть < 1")
    exit()

# Вывод шапки таблицы
print("\n{:^80}".format("Таблица значений функции (1-x)^(-4)"))
print("+---------------+---------------+---------------+---------------+")
print("|      X        |  Приближенное |    Точное     | Членов ряда   |")
print("+---------------+---------------+---------------+---------------+")

# Вычисление и вывод значений
x = xb
while x <= xe + 1e-10:  # Учет погрешности округления
    approx, terms = taylor_series(x, epsilon)
    exact = exact_value(x)

    if exact == exact:  # Проверка на NaN
        print(f"| {x:13.6f} | {approx:13.9f} | {exact:13.9f} | {terms:13d} |")
    else:
        print(f"| {x:13.6f} | {'NaN':^13} | {'NaN':^13} | {'NaN':^13} |")

    x = round(x + dx, 10)

print("+---------------+---------------+---------------+---------------+")