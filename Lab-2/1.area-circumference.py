import math
r = int(input("Enter the radius of circle: "))

#Can use pi as 3.14 but: 

area = math.pi * r * r

perimeter = 2 * math.pi * r

print(f"The perimeter and Area of a circle with radius: {r} is Area: {area} Perimeter: {perimeter}")