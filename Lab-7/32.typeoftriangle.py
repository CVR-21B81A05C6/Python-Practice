a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))

# Check if it's a valid triangle
if a + b > c and a + c > b and b + c > a:
    # Classify by sides
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    # Check for right-angled triangle
    sides = sorted([a, b, c])  # Sort to get the largest side last
    if sides[2]**2 == sides[0]**2 + sides[1]**2:
        print(f"The triangle is {triangle_type} and also a Right-angled triangle.")
    else:
        print(f"The triangle is {triangle_type}, but not right-angled.")
else:
    print("The given sides do not form a valid triangle.")
