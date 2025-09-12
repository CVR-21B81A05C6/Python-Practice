list = [1,2,3,4,5,6]

a = int(input("Enter a number: "))
cnt = 0
for i in list:
    cnt += 1
    if i == a:
        print("Exist")
        break

if(cnt == 6):
    print("doesn't exist")
