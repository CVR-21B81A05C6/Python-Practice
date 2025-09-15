count = 0
n = int(input("Enter the number: "))
temp = n
while n != 0:
    n //= 10
    count += 1

print(f"The number of digits in {temp} are {count}")