class bankaccount:

    def __init__(self):
        self.balance = 0
        self.__privateblnc = 100

    def publicfn(self):
        print(self.__privateblnc)

    def deposite(self, amount): # amount is only argument
        self.balance += amount
        print("deposited")

    def __withdraw(self, amount): # Private
        self.balance -= amount
        print("Withdraw Successfully")

    def __checkblnc(self):
        print("your balance is", self.balance)

    def if_you_are_authentatic(self,Flag):
        if Flag:
            self.__checkblnc()
        else:
            print("Not allowed")

    def if_your_auth_user(self,auth,amount):
        if auth:
            self.__withdraw(amount=amount)
        else:
            print("Not allowed")


icici = bankaccount()
icici.deposite(3000)
password = input("Enter your pin")
if password == '2729':
    icici.if_you_are_authentatic(True)
else:
    print("Invalid Password")
password = input("Enter your pin")
if password == ('2729'):
    icici.if_your_auth_user(True,300)
else:
    print("Invalid")
icici.if_you_are_authentatic(True)
