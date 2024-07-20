class Person:
    name = "John"
    age = None

    def walk(self):
        a = 10 # local  variable
        print('I am walking')
        print(self.age)

John = Person()
John.walk()

class car:
    name = None
    model = None
    color = None

    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color

    def engineStart(self):
        print('Engine started')
        print(self.model)
        print(self.color)
        print(self.name)

BMW = car("BMW", 2019, "Black")
BMW.engineStart()


