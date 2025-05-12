from math import *

x = float(input("Enter the value of X: "))

if -6 < x <= -2:
    y = (-8/9) * ((x + 3.5) ** 2) + 2
elif -2 <= x < 2:
    y = -sqrt(4 - x ** 2)
elif 2 <= x < 8:
    y = log(x, 2) - 1
elif x >= 8:
    y = -2 * x + 18
else:
    print("Out of range. Try again...")

print("X = {0:.2f}  Y = {1:.2f}\n".format(x, y))
