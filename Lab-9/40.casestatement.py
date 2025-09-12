char = input("Enter a character: ")

match char:
    #The if after case _ is a guard condition
    case _ if char.isdigit():
        print("char is a number")
    case _ if char.isupper():
        print("UpperCase")
    case _ if char.islower():
        print("LowerCase")
    #The _ means "match anything"
    case _:
        print("char is a special character")
