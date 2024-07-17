class Password:
    def __init__(self, password="Password"):
        self.__password = password
        self.public_var = 10

    def get_pswd(self, auth):
        if auth:
            print(self.__password)
        else:
            print("Invalid")

    def set_pswd(self, password):
        if len(password) > 10:
            self.__password = password
            print("Password set successfully")
        else:
            print("Invalid password")

pswd = Password("Samarth123")
pswd.get_pswd(True)  # You can call get_pswd with a True or False value to see the password or "Invalid"
pswd.set_pswd("new_secure_password")  # Set a new password that meets the length requirement
pswd.set_pswd("abc")  # This will print "Invalid password"

