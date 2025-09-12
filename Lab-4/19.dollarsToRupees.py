from forex_python.converter import CurrencyRates

dollars = float(input("Enter the amount in $: "))

rupees = 88.33 * dollars

print(f"The amount in Rupees: {rupees}")


#To get live changes based on daily changes: 
#use forex-python : pip install forex-python


c = CurrencyRates()

amount = c.convert('USD','INR',dollars)
print(f"{dollars}$ in rupees is: {amount}INR")
