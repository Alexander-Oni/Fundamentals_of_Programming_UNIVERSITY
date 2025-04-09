from math import *

while True:
    angle = float(input("Enter the value of the angle in degrees: "))
    a = radians(angle)
    if angle % 90 != 0:
        z1 = (sin(a) ** 2 - tan(a) ** 2)/(cos(a) ** 2 - (1/tan(a)) ** 2)
        z2 = tan(a) ** 6
        print("Angle: {0:.2f}\u00b0 Z1: {1:.5f}".format(angle, z1))
        print("Angle: {0:.2f}\u00b0 Z2: {1:.5f}".format(angle, z2))
    else:
        print("Error: incorrect angle value")

