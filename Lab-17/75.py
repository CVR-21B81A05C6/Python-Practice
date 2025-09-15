a = int(input("Enter the first Number: "))
b = int(input("Enter the first Number: "))

while a%b != 0:
    temp = a % b
    a = b
    b = temp

print("The gcd of the given numbers: ",b) 


