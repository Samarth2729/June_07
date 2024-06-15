# Match function
numbers = int(input("Enter a number: "))
match numbers:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Invalid input")

browsers = input("Enter your browser name: ")
match browsers:
    case "Edge":
        print("You have Edge browser")
    case "Safari":
        print("You have Safari browser")
    case "Firefox":
        print("You have Firefox browser")
    case _:
        print("Unknown browser")