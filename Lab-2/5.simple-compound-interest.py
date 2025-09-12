p = int(input("Enter the principle amount: "))
t = int(input("Enter the time duration: "))
r = int(input("Enter the rate of interest: "))

simple = p + p*t*r/100

compound = p * (1 + r/100)**t

print(f"The simple interest and compound interest for the principle: {p} time: {t} rate of interest: {r} is Simple Interest: {simple} Compound Interest: {compound}")