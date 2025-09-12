# Program to calculate volume of a cylinder

import math

r = int(input("Enter the radius: "))
h = int(input("Enter the height: "))

# Volume of cylinder = π * r² * h
volume = math.pi * r ** 2 * h

print(f"The volume of a cylinder with radius {r} and height {h} is {volume}")
