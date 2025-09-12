# Program to calculate simple and compound interest

p = int(input("Enter the principal amount: "))
t = int(input("Enter the time duration (years): "))
r = int(input("Enter the rate of interest: "))

# Simple Interest formula = (P * T * R) / 100
simple_interest = (p * t * r) / 100

# Compound Interest formula = P * (1 + R/100) ^ T
compound_interest = p * (1 + r/100) ** t - p

print(f"The simple interest for principal {p}, time {t}, rate {r}% is {simple_interest}")
print(f"The compound interest for principal {p}, time {t}, rate {r}% is {compound_interest}")
