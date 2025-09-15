m = int(input("Enter the number: "))
n = int(input("Enter the exponent: "))

out = 1
temp = n
while temp != 0:
    out *= m
    temp -= 1

print("The value of m to power of n is: ",out)