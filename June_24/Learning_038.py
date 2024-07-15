class Dog:
    name = None
    colour = None
    age = None
    breed = None

    def eat(self):
        print("Eating")
        return None
    def sleep(self):
        print("Sleeping")

    def bark(self):
        print("Barking")
        return None

bhow = Dog()
bhow.name = "Bhow Bhow"
bhow.colour = "Brown"
bhow.age = 2
bhow.breed = "German Shephard"

chow = Dog()
chow.name = "Chow Chow"
chow.colour = "Black"
chow.age = 3
chow.breed = "Pug"
chow.bark()
chow.eat()
chow.sleep()
print(chow.name)
print(chow.colour)
print(chow.age)
print(chow.breed)


