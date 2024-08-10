class PIMRlogin:

    def __init__(self,email,password):
        self.__email = email
        self.__password = password

    def logincnfrm(self):
        if self.__email == "abc@gmail.com" and self.__password == "123456":
            print("Login Successfully")
        else:
            print("Login Failed")

# this is end of class

student = PIMRlogin("XXXXXXXXXXXXX", "123456")
student.logincnfrm()
# outsider can't change email.