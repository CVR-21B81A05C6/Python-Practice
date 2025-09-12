from datetime import date

birthday = date(2004,1,7)

today = date.today()

age_in_days = today - birthday
 
print(f"Age in days: {age_in_days}")