import math
n = int(input("Enter the number: "))

if str(n) == str(n)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if( n == rev):
    print("Palindrome")
else:
    print("Not Palindrome")