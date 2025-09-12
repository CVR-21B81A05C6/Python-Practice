import math
n = int(input("Enter the number: "))

flag = True
for i in (2,math.sqrt(n)):
    if n % i == 0 and n != i:
        flag = False
        print(False)
        break 

if(flag == True):
    print(True)