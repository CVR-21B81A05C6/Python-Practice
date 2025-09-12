char = input("Enter a vowel character: ").lower()

match char:
    case "a":
        print("Apple")
    case "e":
        print("Elephant")
    case "i":
        print("Iceland")
    case "o":
        print("Orange")
    case "u":
        print("Uruguay")
    case _ :
        print("Enter a vowel")
        
