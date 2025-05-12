from math import *

x = float(input("Enter X: "))
y = float(input("Enter Y: "))
r = float(input("Enter R: "))
flag = 0

if x >= -r and x <= 0 and y >= -x - r and y <= 0 \
    or x >= 0 and x <= r and y <= sqrt(r ** 2 - x ** 2) and y >= 0:
    flag = 1

else:
    flag = 0

print("Point X = {0:.2f}  Y = {1:.2f}".format(x, y), end=" ")

if flag:
    print("will fall into the shaded area")
else:
    print("will not fall into the shaded area")