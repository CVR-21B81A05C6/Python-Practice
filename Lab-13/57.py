nums = []

for i in range (0,10):
    val = int(input("Enter the value to append: "))
    nums.append(val)

pos = 0
neg = 0
zeros = 0

for num in nums:
    if num > 0:
        pos += 1
    elif num<0:
        neg += 1
    else: 
        zeros += 1