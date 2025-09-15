list = []

n = int(input("Enter the size of list: "))

for i in range (0,n):
    val = int(input("Enter the value to append: "))
    list.append(val)

max = list[0]
for i in range(0,n):
    if(list[i] > max):
        max = list[i]

max2 = float('-inf')
for i in range(0,n):
    if(list[i] > max2 and list[i] != max):
        max2 = list[i]

if max2 == float('-inf'):
    print("There is no second largest number.")
else:
    print(f"The second biggest number in the list is: {max2}")