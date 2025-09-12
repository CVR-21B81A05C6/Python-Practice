# Program to calculate age in days

from datetime import date

# Define birthday (YYYY, MM, DD)
birthday = date(2004, 1, 7)

# Get today's date
today = date.today()

# Subtract two dates → gives a timedelta object
age_in_days = today - birthday

print(f"Age in days: {age_in_days}")
