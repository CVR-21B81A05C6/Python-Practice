import math

#Can also use x1 and y1 seperate. This is for one line use of code only
x1 , y1 = map(int, input("Enter the first point: ").split())
x2 , y2 = map(int, input("Enter the Second point: ").split())

distance = math.sqrt((x2-x1) ** 2 + (y2 - y1) ** 2)

print(f"The distance between the points {x1,y1} and {x2,y2} is {distance}")
