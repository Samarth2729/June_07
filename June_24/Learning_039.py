class Account:
    name = None
    ac_number = None
    balance = None

    def deposite(self):
        print("Deposite")
        return None

    def withdraw(self):
        print("Withdraw")
        return None

    def check_balance(self):
        print("Check Balance", self.balance)



sam = Account()
sam.name = "Samarth Rathore"
sam.ac_number = "123456789"
sam.balance = 1000000
sam.deposite()
sam.withdraw()
sam.check_balance()
print(sam.name)