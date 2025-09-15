n = int(input("Enter the number: "))

temp = n
power = 1

while temp !=0:
    power *= n
    temp -= 1

print(f"The value of n to power n: {power}") 