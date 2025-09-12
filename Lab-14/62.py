n = int(input("Enter the number: "))
temp = n
nums = []

digits = 0
while temp > 0:
    nums.append(temp%10)
    temp = temp // 10
    digits += 1

sum = 0
for num in nums:
    sum += num ** digits

if sum == n:
    print(True)
else:
    print(False)