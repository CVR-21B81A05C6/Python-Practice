year = int(input("Enter the year"))

leap = (year % 4 and year % 100 != 0) or (year % 400)

print(f"The year is leap?: {leap}")