balance = 5000

try:
    withdraw = int(input("Enter the amount to withdraw: "))
    if withdraw > balance:
        raise ValueError("Insufficient funds")
except ValueError as e:
    print(e)
else:
    print("Withdraw Successful")
    balance -= withdraw
    print(f"Remaining Balance: {balance}")
finally:
    print("End of the program")
    print("Thank you for using this ATM")




