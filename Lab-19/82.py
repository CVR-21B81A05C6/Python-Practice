arr = []
n = int(input("Enter the size: "))

for i in range(n):
    val = int(input("enter the value: "))
    arr.append(val)

min = arr[0]
for num in arr:
    if(num < min):
        min = num

for num in arr:
    num -= min
    print(num)