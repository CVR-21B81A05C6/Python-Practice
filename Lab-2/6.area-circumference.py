# Program to calculate area and perimeter (circumference) of a circle

import math  # import math module to use math.pi

r = int(input("Enter the radius of circle: "))

# Area of circle = π * r²
area = math.pi * r * r

# Perimeter (circumference) of circle = 2 * π * r
perimeter = 2 * math.pi * r

print(f"The perimeter and area of a circle with radius {r} is Area: {area}, Perimeter: {perimeter}")
