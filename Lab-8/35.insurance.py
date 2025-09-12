marital_status = input("Enter your marital Status: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")

if marital_status:
    print(True)
else:
    if gender.lower() == "male":
        if age >= 30:
            print(True)
        else:
            print(False)
    else:
        if age >= 25:
            print(True)
        else:
            print(False)
