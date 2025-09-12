import math

a = float(input("Enter the length of side: "))
b = float(input("Enter the length of side: "))
c = float(input("Enter the length of side: "))

s = (a+b+c)/2
area = math.sqrt(s * (s-a) * (s-b) * (s-c))

print(f"The area of a triangle with sides : {a} {b} {c} is {area}")