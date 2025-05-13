from math import *

print("Enter Xbeg, Xend, Dx")

xb = float(input("Xbeg = "))
xe = float(input("Xend = "))
dx = float(input("Dx = "))

print(f"Xbeg = {xb:7.2f}  Xend = {xe:7.2f}  Dx = {dx:7.2f}\n")

xt = xb

print("+---------+---------+")
print("|    X    |    Y    |")
print("+---------+---------+")

while xt < xe:
    if -6 <= xt <= -2:
        y = (-8/9) * ((xt + 3.5) ** 2) + 2
    elif -2 <= xt < 2:
        y = -sqrt(4 - xt ** 2)
    elif 2 <= xt < 8:
        y = log(xt, 2) - 1
    else:
        y = -2 * xt + 18
    print(f"| {xt:7.2f} | {y:7.2f} |")
    xt += dx
print("+---------+---------+")
