arr = []
for _ in range(10):
    val = int(input("Enter the value: "))
    arr.append(val)

sum = 0
for i in range(10):
    sum += arr[i]
    if(arr[i] == 0):
        arr[i] = sum

for num in arr:
    print(num)