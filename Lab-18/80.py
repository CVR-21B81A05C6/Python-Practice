freq = []
arr = []

n = int(input("enter the size: "))
for i in range(n):
    val = int(input("enter the value: "))
    arr.append(val)

#for i in arr:
    #cnt = 0
    #for j in arr:
        #if i == j:
            #cnt += 1
    
    #freq.append([i,cnt])

seen = set()
for i in arr:
    if i not in seen:
        cnt = arr.count(i)
        freq.append([i, cnt])
        seen.add(i)

for i in freq:
    print(i)