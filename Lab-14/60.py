n = int(input("Enter the number: "))

sum = 0
half = n // 2 + 1
for i in range(1,half):
    if n % i == 0:
        sum += i

if sum == n:
    print(True)
else:
    print(False)