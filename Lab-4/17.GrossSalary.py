basic = float(input("Enter your basic salary: "))

da = 0.40 * basic
hra = 0.20 * basic
gross = basic + da + hra

print(f"The gross salary for basic salary: {basic} is {gross}")