# Multilevel Inheritance

class Grandfather:

    def BMW(self):
        print("This is Grandfather's BMW")

class Father(Grandfather):

    def Audi(self):
        print("This is Father's Audi")

class child(Father):

    def Bucati(self):
        print("This is child's Bucati")


Child = child()
Child.BMW()
Child.Audi()
Child.Bucati()
