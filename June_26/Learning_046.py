# Encapsulation
# bind the data variables with methods
# Data member -/ class variable
# Member functions -/ class method
# wrapping or binding the data variables with the methods is called encapsulation

class car:
    name = None
    password = 1243

    # Home

    def __init__(self):
        print("I am called automatically when the object is created")

    def chang_pswd(self):
        self.password = 4567

# Outsider
BMW = car() # instance
car.password = 4567 # this is class variable

# So the access of change the password is given to only home not outsider

