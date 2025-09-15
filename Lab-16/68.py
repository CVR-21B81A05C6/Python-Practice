n = int(input("Enter the number to find the factorial: "))
temp = n
fact = 1

while temp != 0:
    fact *= temp
    temp -= 1

print(f"The factorial of the number {n} is {temp}")