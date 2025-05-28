from math import *

def calculate_z1(a):
    return (sin(a) ** 2 - tan(a) ** 2) / (cos(a) ** 2 - (1 / tan(a)) ** 2)

def calculate_z2(a):
    return tan(a) ** 6


def process_angles(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            try:
                angle = float(line.strip())
                a = radians(angle)
                if angle % 90 != 0:
                    z1 = calculate_z1(a)
                    z2 = calculate_z2(a)
                    outfile.write(f"Angle: {angle:.2f}° Z1: {z1:.5f}\n")
                    outfile.write(f"Angle: {angle:.2f}° Z2: {z2:.5f}\n")
                else:
                    outfile.write(f"Error: incorrect angle value {angle:.2f}°\n")
            except ValueError:
                outfile.write(f"Error: invalid input '{line.strip()}'\n")

# Основная программа
if __name__ == "__main__":
    input_filename = "Файлы_для_первой_лабы/Входные_данные.txt"  # Файл с входными данными
    output_filename = "Файлы_для_первой_лабы/Выходной_файл.txt"  # Файл для результатов

    process_angles(input_filename, output_filename)
    print(f"Обработка завершена. Результаты сохранены в {output_filename}")