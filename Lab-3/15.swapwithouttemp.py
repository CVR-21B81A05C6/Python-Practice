a = int(input("Enter the value: "))
b = int(input("Enter the value: "))

print(f"The numbers before swapping a: {a} b: {b}")

a = a + b
b = a - b
a = a - b

print(f"The numbers after swapping a: {a} b: {b}")
