n = int(input("Enter the decimal value: "))

out = ""
while(n!=0):
    out = str(n%8) + out
    n //= 8

print(out)