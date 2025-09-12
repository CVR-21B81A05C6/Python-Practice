char = input("Enter a character: ")

if char.isdigit():
    print("char is a number")
elif char.isupper():
    print("UpperCase")
elif char.islower():
    print("LowerCase")
else:
    print("char is a special character")
