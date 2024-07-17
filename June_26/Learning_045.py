# So in 044 we use constructor to create object of class
# now we use without constructor to create object of class
class PIMRlogin:
    email = None
    password = None

    def login(self):
        if self.password == 'Sam123':
            print('I am logged in')
        else:
            print('Incorrect password')

# this is the end of class

Studentlogin = PIMRlogin()
Studentlogin.email = 'Samarth@1223' # we need to do manually >>>>>
Studentlogin.password = 'Sam123'
Studentlogin.login()
