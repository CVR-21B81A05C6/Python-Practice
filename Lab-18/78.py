nums = []

n = int(input("Enter the size of list: "))

for i in range(n):
    val = int(input("Enter the value to append: "))
    nums.append(val)

max1 = max(nums)
max2 = float('-inf')
maxPos = -1
for i in range(n):
    if nums[i] != max1 and nums[i] > max2:
        max2 = nums[i]
        maxPos = i

if max2 == float('-inf'):
    print("There is no second largest number.")
    max2 = None

min1 = min(nums)
min2 = float('inf')
minPos = -1
for i in range(n):
    if nums[i] != min1 and nums[i] < min2:
        min2 = nums[i]
        minPos = i

if min2 == float('inf'):
    print("There is no second smallest number.")
    min2 = None

if max2 is not None and min2 is not None:
    nums[minPos], nums[maxPos] = max2, min2

for i in nums:
    print(i)
