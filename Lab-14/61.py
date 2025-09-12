n = int(input("Enter the value: "))

square = n ** 2;

if square % 10 == n % 10:
    print(True)
else:
    print(False)