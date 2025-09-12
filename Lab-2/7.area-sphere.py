# Program to calculate surface area of a sphere

import math

r = int(input("Enter the value of radius: "))

# Surface area of sphere = 4 * π * r²
area = 4 * math.pi * r ** 2

print(f"The area of a sphere with radius {r} is {area}")
