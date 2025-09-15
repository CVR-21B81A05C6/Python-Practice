n = int(input("Enter a number: "))
temp = n
rev = 0
count = 0

while temp != 0:
    temp //= 10
    count += 1

temp = n

while temp != 0:
    count -= 1
    rev += (temp % 10) * (10 ** (count))
    temp //= 10

print(f"Reverse of number: {n} is: {rev}")