# Try,except,finally>>>>>

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:

    print("This will always execute.")

class XYZ:

    try:
        a = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    else:
        print(a)
    finally:

        print("This will always execute.")