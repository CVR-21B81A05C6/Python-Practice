import math
for i in range(2,100):
    flag = 1
    for j in range (2,int(math.sqrt(i)) + 1):
        if i % j == 0:
            flag = 0
    if(flag == 1):
        print(f"{i} is a prime number")
