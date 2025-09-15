n = int(input("Enter the number of 6 place values: "))

if(len(str(n)) > 6):
    n = int(input("Enter the number of 6 place values: "))



sumOfEvenDigits = 0
productOfOddDigits = 1

temp = n
count = 0
while temp != 0:
    temp //= 10
    count += 1

temp = n
while count != 0:
    if(count % 2 == 1):
        productOfOddDigits *= temp%10
        temp //= 10
    else:
        sumOfEvenDigits += temp%10
        temp //= 10
    count -= 1


print(f"Sum of Even Digits = {sumOfEvenDigits} and Product of odd digits = {productOfOddDigits}")