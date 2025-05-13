from math import *
from random import *

r = float(input("Enter R: "))
flag = 0

print("+---------+---------+---------+")
print("|    X    |    Y    |  Result |")
print("+---------+---------+---------+")

for n in range(10):
    x = uniform(-r, r)
    y = uniform(-r, r)
    if x >= -r and x <= 0 and y >= -x - r and y <= 0 \
        or x >= 0 and x <= r and y <= sqrt(r ** 2 - x ** 2) and y >= 0:
        flag = 1
        result = "Yes"
    else:
        flag = 0
        result = "No"

    print(f"| {x:7.2f} | {y:7.2f} | {result:^7} |")

print("+---------+---------+---------+")
