a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
op = input("Enter operator: ")

match op:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case _ :
        print("Enter valid operator")