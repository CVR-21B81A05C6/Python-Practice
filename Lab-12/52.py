rows = 5
cols = 20
for row in range(rows):
    for col in range(cols):
        num = row + 1 + col * rows
        if num <= 99:
            print(f"{num:3}",end=" ")
    print()