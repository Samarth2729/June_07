# Polymorphism
# Method Overriding
class Shape:
    def area(self):
        print("Area of the shape")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

rect = Rectangle(5, 3)
print(rect.area())  # Output: 15
circle = Circle(4)
print(circle.area())  # Output: 50.24
shape = Shape()
shape.area()  # Output: Area of the shape
