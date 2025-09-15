arr = []
n = int(input("enter the size: "))

for i in range(n):
    val = int(input("Enter the value: "))
    arr.append(val)

neg = []
for num in arr:
    if(num < 0):
        neg.append(num)
        arr.remove(num)

for num in neg:
    arr.append(num)

for num in arr:
    print(num,end="\t")

    