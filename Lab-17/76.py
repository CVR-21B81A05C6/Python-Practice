a = int(input("Enter the first Number: "))
b = int(input("Enter the first Number: "))

def gcd(var1,var2):
    while var1%var2 != 0:
        temp = var1 % var2
        var1 = var2
        var2 = temp
    return var2

lcm = abs(a*b) // gcd(a,b)
print("The LCM of numbers:",a,b,"is:",lcm)