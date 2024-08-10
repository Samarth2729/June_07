print("Start of the programm")
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)

except Exception as e:
    print(e)
    print("An error occurred. Please try again with valid input.")
    print("End of the programm")

# Errors are something , difficult to recover.
# errors have more severe issues that typically prevent
# the proramm from running
# impossible
# syntax , indentation

# Exception error can be handled
# Exception are events that occurs during the execution of the
# programm .. recover can be possible