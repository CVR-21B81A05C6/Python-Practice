n = int(input("Enter the decimal value: "))

hex_map = {
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}

out = ""

while(n != 0):
    remainder = (n%16)
    if(remainder >= 10):
        val = hex_map[remainder]
    else:
        val = str(remainder)
    out = val + out
    n //= 16

print(out)

