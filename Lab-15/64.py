n = int(input("Enter the number: "))

sumOfDigits = 0
productOfDigits = 1
temp = n

while(temp != 0):
    sumOfDigits += temp % 10
    temp //= 10

temp = n
while(temp != 0):
    productOfDigits *= temp % 10
    temp //= 10

print(f"Sum of Digits: {sumOfDigits} Product of Digits: {productOfDigits}")