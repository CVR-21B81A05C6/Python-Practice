list = [];

for i in range(0,9):
    val = int(input("Enter the value: "))
    list.append(val)

for i in range(0,9):
    print(list[i],end="\t")
    if(i%3 == 2):
        print()
