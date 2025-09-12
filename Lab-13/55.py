list = []

n = int(input("Enter the size of list: "))

for i in range (0,n):
    val = int(input("Enter the value to append: "))
    list.append(val)

max = list[0]
for i in range(0,n):
    if(list[i] > max):
        max = list[i]

print(f"The maximum value present in the list is {max}")