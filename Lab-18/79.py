names = []
sales = []
n = 5
months = 6

for _ in range(n):
    val = input("enter the name: ")
    names.append(val)


for _ in range(n):
    person_sales = []
    for _ in range(months):
        sale = float(input("Enter the sales in the following month: "))
        person_sales.append(sale)
    sales.append(person_sales)

individual_sales = []

for i in range(n):
    sum = 0
    for j in range(months):
        sum += sales[i][j]
    individual_sales.append(sum)
    print(sum)

total_sales = 0

for i in individual_sales:
    total_sales += i

print(total_sales)
