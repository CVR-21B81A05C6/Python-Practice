import math

def quadratic_roots(a, b, c):
    D = b**2 - 4*a*c
    print(f"Discriminant (D) = {D}")
    
    if D > 0:
        root1 = (-b + math.sqrt(D)) / (2*a)
        root2 = (-b - math.sqrt(D)) / (2*a)
        nature = "Real and Distinct"
    elif D == 0:
        root1 = root2 = -b / (2*a)
        nature = "Real and Equal"
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-D) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        nature = "Complex Conjugates"
        
    return root1, root2, nature

# Example usage
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

r1, r2, nature = quadratic_roots(a, b, c)
print(f"The roots are: {r1} and {r2}")
print(f"Nature of roots: {nature}")

