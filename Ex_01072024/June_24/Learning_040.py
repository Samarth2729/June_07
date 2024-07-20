# Constructor ?
# Use to initilize the values
# of the instance variables (attributes)
#
# __init__ method is called constructor
''


class Computer:

    def __init__(self): # Default constructor with no arguments
        print('in init')
    def __init__(self, name, id): # Parameterized Constructor
        self.name = name
        self.id = id

    def updated(self):
        print('Updated', self.name, self.id)


C1 = Computer('Mac', 1)
C2 = Computer('HP', 2)
print(f'{C1.name} has id {C1.id}')
print(f'{C2.name} has id {C2.id}')

C1.updated()
C2.updated()


