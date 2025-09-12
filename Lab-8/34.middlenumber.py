a = int(input("Enter the 3 digit number: "))

if(a // 1000 != 0):
    a = int(input("Enter the 3 digit number: "))

ones_digit = a % 10;
tens_digit = (a%100 - ones_digit)/10
hundered_digit = (a%1000 - tens_digit*10 - ones_digit)/100

if tens_digit == ones_digit + hundered_digit:
    print(True)
else:
    print(False)
