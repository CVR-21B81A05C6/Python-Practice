val1 = int(input("Enter the number"))
val2 = int(input("Enter the number"))
val3 = int(input("Enter the number"))

if val1 > val2:
    if val1 > val3:
        print(f"{val1} is biggest")
    else:
        print(f"{val3} is biggest")
else:
    if val2 > val3:
        print(f"{val2} is biggest")
    else:
        print(f"{val3} is biggest")