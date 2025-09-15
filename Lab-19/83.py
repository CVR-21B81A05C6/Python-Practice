arr = []

for i in range(10):
    val = int(input("enter the value: "))
    arr.append(val)

first5 = arr[:5]
remaining = arr[5:]


arr = remaining + first5

for num in arr:
    print(num)