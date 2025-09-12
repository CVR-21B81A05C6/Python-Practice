a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

match a - b:
    case diff if diff > 0:
        print(a)
    case diff if diff < 0:
        print(b)
    case _ :
        print(f"Same number {a}")
