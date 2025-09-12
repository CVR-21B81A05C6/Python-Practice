nums = []

n = int(input("Enter the size of list: "))


for i in range (0,n):
    val = int(input("Enter the value to append: "))
    nums.append(val)

min = nums[0]
for i in range(0,n):
    if(nums[i] < min):
        min = nums[i]

min2 = float('inf')
for i in range(0,n):
    if(min < nums[i] < min2):
        min2 = nums[i]

print(f"The 2nd min value present in the list is {min2}")