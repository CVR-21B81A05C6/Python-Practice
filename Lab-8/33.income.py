sales = int(input("Enter the sales: "))

if sales >= 50000:
    income = 375 + 0.16*sales
elif sales >= 40000:
    income = 350 + 0.14*sales
elif sales >= 30000:
    income = 325 + 0.12*sales
elif sales >= 20000:
    income = 300 + 0.09*sales
elif sales >= 10000:
    income = 275 + 0.05*sales
else:
    income = 250 + 0.03*sales

print(income)