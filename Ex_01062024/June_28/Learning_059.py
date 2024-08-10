# Abstraction -- OOPs
# Hiding the implementation details and showing only the essential features to the user.
# Abstract class
from abc import ABC, abstractmethod
# Importing necessary modules


# Abstract method is incomplete method without a body.
class Animal(ABC):
    def __init__(self, name):
        self.name = name
        @abstractmethod
        def sound(self):
            pass
class Dog(Animal):
    def sound(self):
        return "Bark"

class  Cat(Animal):
    def sound(self):
        return "Meow"

dog = Dog("Lolu")
cat = Cat("Tom")
print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow
