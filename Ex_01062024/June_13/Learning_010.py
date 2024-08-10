number1 = int(input("Enter the number1\n"))
number2 = int(input("Enter the number2\n"))
number3 = int(input("Enter the number3\n"))
if number1 > number2 and number1 > number3:
    print("number1 is greater")
elif number2 > number1 and number2 > number3:
    print("number2 is greater")
elif number3 > number1 and number3 > number2:
    print("number3 is greater")
else:
    print("All are equal")