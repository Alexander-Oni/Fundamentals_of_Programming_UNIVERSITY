from math import *

def calculate_z1(a):
    return (sin(a) ** 2 - tan(a) ** 2) / (cos(a) ** 2 - (1 / tan(a)) ** 2)

def calculate_z2(a):
    return tan(a) ** 6

while True:
    angle = float(input("Enter the value of the angle in degrees: "))
    a = radians(angle)
    if angle % 90 != 0:
        z1 = calculate_z1(a)
        z2 = calculate_z2(a)
        print("Angle: {0:.2f}\u00b0 Z1: {1:.5f}".format(angle, z1))
        print("Angle: {0:.2f}\u00b0 Z2: {1:.5f}".format(angle, z2))
    else:
        print("Error: incorrect angle value")

