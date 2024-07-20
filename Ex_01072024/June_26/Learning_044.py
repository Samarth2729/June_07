class PIMRlogin:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self):
        if self.password == 'Sam123':
            print('Login successfully')
        else:
            print('Invalid password')



Studentlogin = PIMRlogin("Samarth@gmail.com", "Sam123")
Studentlogin.login()

