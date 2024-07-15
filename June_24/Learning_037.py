class Person:
    # Attributes
    name = None
    age = None
    id = None
    phone_num = None

    # Behaviour
    def walk(self): # No argument no return
        print("I am walking")

    def eat(self): # One argument no return
        print("I am eating")
        print("Eating",self.name)

    def sleep(self): # No argument but one return
        print("I am sleeping")
        return None

    def work(self): # One argument and one return
        print("I am working")
        return None

# Create object of class
sam = Person()
sam.name = "Sam"
sam.walk()
sam.eat()

Kosh = Person()
Kosh.name = "Kosh"
Kosh.walk()
Kosh.eat()
Kosh.sleep()


