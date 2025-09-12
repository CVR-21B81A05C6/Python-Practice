from datetime import timedelta
sec = int(input("Enter number of seconds: "))

td = timedelta(seconds = sec)

print(str(td));

# another solution

hours = sec // 3600
remaining_seconds = sec%3600

minutes = remaining_seconds // 60
seconds = remaining_seconds%60

print(f"Converted value of seconds: {sec} to hours-minutes-seconds is {hours}:{minutes}:{seconds}")