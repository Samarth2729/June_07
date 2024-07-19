# What is Inheritance ?
# Aquire the Attributes and Behaviors.
# Data members and methods

# Concept in object oriented programming.
# that allows a class to inherit the attributes and methods of another class.
# The class that inherits is called the child class,
# and the class that is inherited is called the parent class.

# Types of Inheritance
# >>>>>>>>>>>>>>>>>>>>
# Single Inheritance - 80% of times single Inheritance will be used.
# Multiple Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Hybrid Inheritance
# Example of single Inheritance>>>

class Grandfather: # this is called parent class and base claas
    key = "abc123"

    def grandfather_method(self):
        print("I am a grandfather")


class Father(Grandfather): # Child class,sub class
    def father_method(self): # return type functions

        print("I am a father")


parent = Father()
print(parent.key)
parent.grandfather_method()
parent.father_method()
