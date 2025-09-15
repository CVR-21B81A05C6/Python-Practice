n = int(input("Enter the decimal number: "))

ans = "";

while(n != 0):
    val = 1 if n % 2 == 1 else 0
    ans = str(val) + ans
    n //= 2

print(ans)

binary = (input("Enter a binary number: "))
power = len(binary) - 1
ans = 0
for char in binary:
    ans += int(char) * 2 ** power
    power -= 1

print(ans)

