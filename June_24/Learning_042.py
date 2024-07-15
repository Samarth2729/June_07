class Student():
    def __init__(self):
        self.name = input("Enter name: ")
        self.marks = int(input("Enter marks: "))

    def display(self):
        print("Name: ", self.name)
        print("Marks: ", self.marks)

S1 = Student()
S1.display()