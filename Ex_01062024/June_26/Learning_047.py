class Car:
    def __init__(self):
        # Home
        self._private_var = "private123"
        self.__protect_var = "protected123"
        self.public_var = "public123"

    def __private_method(self):
        print("Private method called")

    def printname(self):
        if self._private_var == 'private123':
            print("Private variable accessed")
        print("accessed")

# So only within the home class can access the private and protected fnc
# Outsider Can't access

# Outsider
bmw = Car() # instance
bmw.printname()
