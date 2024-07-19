# One more example of polymorphism Overridding method

class Father:
    def bike(self):
        print('Hero Honda')

class Son(Father):
    def bike(self):
        super().bike()
        print('Honda Activa')

child = Son()
child.bike()

# Onto Method Overloading
# Python doesn't support method overloading
# in traditional sense.

class Mathutils(object):

    def add(self, a, b=0,c=0):
        return a + b + c

    # def add(self, a, b, c):
    #     return a + b + c
    # This will give error
    # TypeError: Mathutils.add() takes 2 positional arguments but 3 were given.
    # because python doesn't support traditional sense

math = Mathutils()
op0 = math.add(1)
op1 = math.add(1, 2)
op2 = math.add(1, 2, 3)
print(op0, op1, op2)



