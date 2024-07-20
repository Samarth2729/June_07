class mycustomexception(Exception):
    def __init__(self,  message):
        self.message = message
        super().__init__(message)

# super().__init__() # >> this will call the constructor of the parent class
        # super().__init__(message) # >> this will call the constructor of the parent class and pass the message to it

balance = 1000
withdraw = int(input("Enter the amount to withdraw: "))
if withdraw > balance:
    raise mycustomexception("Insufficient funds")
else:
    print("Withdraw Successful")
    print(f"Remaining Balance: {balance-withdraw}")


